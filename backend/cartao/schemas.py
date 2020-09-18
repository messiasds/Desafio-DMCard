#from . import ma
from marshmallow import post_load, Schema, fields
from .models import Solicitacao

#class SolicitacaoSchemaResumo

class SolicitacaoSchema(Schema):

    renda = fields.Decimal(as_string=True)
    credito = fields.Decimal(as_string=True)
    data_nascimento = fields.Date('%Y-%m-%d')

    class Meta:
        fields = ("id", "nome","rg", "cpf", "renda", "telefone", "email", 
                  "cartao_aprovado", "credito","pontuacao","data_nascimento" )

solicitacao_schema_muitos =  SolicitacaoSchema(many=True)
solicitacao_schema = SolicitacaoSchema()

class SolicitacaoSchemaPost(Schema):

    nome = fields.Str()
    data_nascimento = fields.Date('%Y-%m-%d')
    rg = fields.Str()
    cpf = fields.Str()
    renda = fields.Decimal()
    telefone = fields.String()
    email = fields.String() # trocar por Email
    cartao_aprovado = fields.Boolean()
    credito = fields.Decimal()
    pontuacao = fields.Int()
    
    @post_load
    def converter_objeto(self, data, **kwargs):
        # converte o dicionário em no objto Solicitacao
        return Solicitacao(**data)

solicitacao_schema_post = SolicitacaoSchemaPost()