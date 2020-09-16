from flask import Flask
from flask import abort
from flask import request
from flask import Response
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load, Schema, fields
import regras as regras_negocio

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app) 

#app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# MODELS
class Solicitacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    rg = db.Column(db.String(11), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    renda = db.Column(db.Float, nullable=False)
    telefone = db.Column(db.String(20), nullable=False) 
    email = db.Column(db.String(100), nullable=False)
    cartao_aprovado = db.Column(db.Boolean, nullable=True)
    credito = db.Column(db.Float, nullable=True )
    pontuacao = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Solicitacao %r>' % self.nome 

class SolicitacaoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome","rg", "cpf", "renda", "telefone", "email", 
                  "cartao_aprovado", "credito","pontuacao" )

solicitacao_schema_muitos =  SolicitacaoSchema(many=True)
solicitacao_schema = SolicitacaoSchema()

# Refatorar para usar apenas o Schema do marsmallow padrao

class SolicitacaoSchemaPost(Schema):
    nome = fields.Str()
    data_nascimento = fields.Date('%Y-%m-%d')
    rg = fields.Str()
    cpf = fields.Str()
    renda = fields.Float()
    telefone = fields.String()
    email = fields.String() # trocar por Email
    cartao_aprovado = fields.Boolean()
    credito = fields.Float()
    pontuacao = fields.Int()
    
    @post_load
    def converter_objeto(self, data, **kwargs):
        # converte o dicionário em no objto Solicitacao
        return Solicitacao(**data)

solicitacao_schema_post = SolicitacaoSchemaPost()

# VIEWS
@app.route('/')
def inicio():
    return "API em flask"

@app.route('/teste/<renda>/', methods=['GET'])
def teste(renda):
    renda = int(renda)
    credito = regras.aprovar_credito(700, renda)
    return "O credito eh " + str(credito) 

@app.route('/solicitacoes', methods=['GET'])
def mostrar_todas_solicitacoes():
    ret = Solicitacao.query.all()
    #return solicitacao_schema.dumps(ret)
    return solicitacao_schema_muitos.jsonify(ret)

@app.route('/solicitacoes/<int:id>', methods=['GET'])
def solicitacao_detalhes(id):
    try:
        solicitacao = Solicitacao.query.get(id)
    except:
        abort(404)

    return solicitacao_schema.jsonify(solicitacao)

@app.route('/solicitacoes', methods=['POST'])
def salvar_solicitacao():

    ''' Salva a solicitacao de cartão e atualiza os limites de crédito 
    '''
    
    request_dados = request.json
    renda = float(request_dados['renda'])

    pontuacao = regras_negocio.gerar_pontuacao()
    credito = regras_negocio.aprovar_credito(pontuacao, renda)

    solicitacao_obj = solicitacao_schema_post.load(request_dados)

    solicitacao_obj.credito = credito
    solicitacao_obj.pontuacao = pontuacao

    if credito > 0:
        solicitacao_obj.cartao_aprovado = True       
    else:
        solicitacao_obj.cartao_aprovado = False

    db.session.add(solicitacao_obj)
    db.session.commit()
    
    return Response(status=201)

@app.route('/solicitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):

    try:
        obj = Solicitacao.query.get(id)
        resp = db.session.delete(obj)
        db.session.commit()

    except:
        abort(404)

    return Response(status=200)

app.run()

