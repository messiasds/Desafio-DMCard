from flask import Flask
from flask import request
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load, Schema, fields
import regras

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

    def __repr__(self):
        return '<Solicitacao %r>' % self.nome 

class SolicitacaoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome","rg", 
        "cpf", "renda", "telefone", "email" )

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
    print(credito)
    return "O credito eh " + str(credito) 

@app.route('/solicitacoes', methods=['GET'])
def mostrar_todas_solicitacoes():
    ret = Solicitacao.query.all()
    #return solicitacao_schema.dumps(ret)
    return solicitacao_schema_muitos.jsonify(ret)

@app.route('/solicitacoes/<int:id>', methods=['GET'])
def mostrar_solicitacao(id):

    solicitacao = Solicitacao.query.get(id)
    return solicitacao_schema.jsonify(solicitacao)

@app.route('/solicitacoes', methods=['POST'])
def criar_solicitacao():

    resp = solicitacao_schema_post.load(request.json)
    db.session.add(resp)
    db.session.commit()
    
    return "rota criar solicitacao"

@app.route('/solicitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):

    obj = Solicitacao.query.get(id)
    resp = db.session.delete(obj)
    db.session.commit()
    return "deletado"



app.run()

