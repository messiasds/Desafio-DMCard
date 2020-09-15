from flask import Flask
from flask import request
from markupsafe import escape
import regras

app = Flask(__name__)

@app.route('/')
def inicio():
    return "API em flask"

@app.route('/teste/<renda>/', methods=['GET'])
def teste(renda):
    renda = int(f"{renda}")
    credito = regras.aprovar_credito(700, renda)
    print(credito)
    return "O credito eh " + str(credito) 

@app.route('/solitacoes', methods=['GET'])
def mostrar_todas_solicitacoes():
    return "rota mostrar todas"

@app.route('/solicitacoes/<int:id>', methods=['GET'])
def mostrar_solicitacao():
    return "rota mostrar solicitacao"

@app.route('/solitacoes', methods=['POST'])
def criar_solicitacao():
    return "rota criar solicitacao"

@app.route('/solitacoes/<int:id>', methods=['DELETE'])
def excluir_solicitacao():
    return "rota excluir"

 

app.run()