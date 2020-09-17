# regras de negócio

import random

def gerar_pontuacao():
    return random.randint(1,999)

def aprovar_credito(pontuacao, renda):
    '''
    verifica o credito para cada solicitacao baseada em sua pontuacao '''

    lista_pontuacoes = [
        { 'inicio':1, 'limite':299, 'credito':0} ,
        { 'inicio':300, 'limite':599, 'credito' : 1000},
        { 'inicio':600, 'limite':799, 'credito': percentual_por_renda(50, renda, cred_min=1000)},
        { 'inicio':800, 'limite':950, 'credito': percentual_por_renda(200, renda)},
        { 'inicio':951, 'limite':999, 'credito': 1000000 }    
        ]

    for linha in lista_pontuacoes:
        if pontuacao >= int(linha['inicio']) and pontuacao <= int(linha['limite']):
            return linha['credito']


def percentual_por_renda(percentual, renda, cred_min = None):

    ''' retorna o valor do crédito baseado calculado com percentual da renda informada
        avaliando o credito minimo caso disponivel '''

    credito =  (renda * percentual) / 100

    if credito < 1000:
        return cred_min
    
    return credito





