from . import db

class Solicitacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    rg = db.Column(db.String(11), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    renda = db.Column(db.Numeric(10,2), nullable=False)
    telefone = db.Column(db.String(20), nullable=False) 
    email = db.Column(db.String(100), nullable=False)
    cartao_aprovado = db.Column(db.Boolean, nullable=True)
    credito = db.Column(db.Numeric(10,2), nullable=True ) #mudei pra decimal
    pontuacao = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Solicitacao %r>' % self.nome 