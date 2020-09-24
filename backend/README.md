## Backend do Desafio



    Nome:
    Data_nascimento:
    cpf:
    rg:
    telefone:
    email:
    renda:
    pontuacao:
    credito:




## Tecnologias 

* Python
* Flask
* SqlAchemy (ORM)

## Rotas da API

Api possui 3 funcionanlidades: Listar todos, Listar detalhes da solicitação e excluir solicitação

Exemplo de Retorno da API

```json
[
  {
    "id": 3, 
    "nome": "Messias da Silva", 
    "rg": "4003522211", 
    "cpf": "33344455522", 
    "telefone": "(12)982150000",
    "email": "messiasds@gmail.com", 
    "renda": 100.0,
    "cartao_aprovado": true, 
    "pontuacao": 980, 
    "credito": 1000000.0 

  }
]

```

campos **cartao_aprovado** , **potuacao** , **credito** são gerados com base nas regras de negócio do desafio



**Rotas:**

GET /solicitacoes - Exibe todas as solicitações de cartão

GET /solicitacoes/{id} - Motra os detalhes da solicitação específicada pelo id

POST /solicitacoes - cria uma nova solicitação de cartão 

DELETE /solicitacoes/{id} - Exclui a solicitação selecionada específicada pelo id




