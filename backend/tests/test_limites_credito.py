# Testa as regras relacionadas ao limite de crédito

from ..cartao import regras
import random

''' regras 
Score        Credito
1 a 299	    0
300 a 599	R$ 1000,00
600 a 799	50% da renda credito minimo 1000
800 a 950	200% da renda 
951 a 999	R$ 1.000.000 '''


def test_reprovado():

    ''' Testa score de 1 a 299 '''

    score = random.randint(1,299)
    renda = 900
    credito = regras.aprovar_credito(score, renda)
    assert credito == 0 

def test_credito_1000():

    ''' Testa score de 300 a 599 '''

    score = random.randint(300,599)
    renda = 900
    credito = regras.aprovar_credito(score, renda)
    assert credito == 1000

def test_credito_ilimitado():

    ''' Testa score de 951 a 999 '''
    
    score = random.randint(951,999)
    renda = 900
    credito = regras.aprovar_credito(score, renda)
    assert credito == 1000000

def test_credito_50_porcento_credito_min():

    ''' Testa score de 600 a 799 com credito minimo de 1000 '''

    score = random.randint(600,799)
    renda = 900
    credito = regras.aprovar_credito(score, renda)
    assert credito == 1000

def test_credito_50_porcento():

    ''' Testa score de 600 a 799 com crédito acima do crédito mínimo '''
    
    score = random.randint(600,799)
    renda = 3500
    credito = regras.aprovar_credito(score, renda)
    assert credito == 1750

def test_credito_200_porcento():

    ''' Testa score de 800 a 950 com acima do crédito mínimo '''

    score = random.randint(800,950)
    renda = 900
    credito = regras.aprovar_credito(score, renda)
    assert credito == 1800

