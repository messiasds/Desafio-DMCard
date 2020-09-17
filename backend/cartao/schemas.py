from . import ma
from marshmallow import post_load, Schema, fields
from .models import Solicitacao

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