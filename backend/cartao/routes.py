from flask import abort
from flask import request
from flask import Response
from flask import Blueprint
from flask import jsonify
from markupsafe import escape
from . import regras as regras_negocio
from . import db
from .models import Solicitacao
from . import schemas


cartao = Blueprint('cartao', __name__)

@cartao.route('/')
def inicio():
    return "API em flask"

@cartao.route('/teste/<renda>/', methods=['GET'])
def teste(renda):
    renda = int(renda)
    credito = regras.aprovar_credito(700, renda)
    return "O credito eh " + str(credito) 

@cartao.route('/solicitacoes', methods=['GET'])
def mostrar_todas_solicitacoes():
    ret = Solicitacao.query.all()
    return schemas.solicitacao_schema_muitos.dumps(ret, many=True)
    #return schemas.solicitacao_schema_muitos.jsonify(ret)

@cartao.route('/solicitacoes/<int:id>', methods=['GET'])
def solicitacao_detalhes(id):
    try:
        solicitacao = Solicitacao.query.get(id)
    except:
        abort(404)

    return schemas.solicitacao_schema.dumps(solicitacao)
    #return schemas.solicitacao_schema.jsonify(solicitacao)

@cartao.route('/solicitacoes', methods=['POST'])
def salvar_solicitacao():

    ''' Salva a solicitacao de cartão e atualiza os limites de crédito 
    '''
    
    request_dados = request.json
    renda = float(request_dados['renda'])

    pontuacao = regras_negocio.gerar_pontuacao()
    credito = regras_negocio.aprovar_credito(pontuacao, renda)

    solicitacao_obj = schemas.solicitacao_schema_post.load(request_dados)

    solicitacao_obj.credito = credito
    solicitacao_obj.pontuacao = pontuacao

    if credito > 0:
        solicitacao_obj.cartao_aprovado = True       
    else:
        solicitacao_obj.cartao_aprovado = False

    db.session.add(solicitacao_obj)
    db.session.commit()
    
    return Response(status=201)

@cartao.route('/solicitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):

    try:
        obj = Solicitacao.query.get(id)
        resp = db.session.delete(obj)
        db.session.commit()

    except:
        abort(404)

    return Response(status=200)