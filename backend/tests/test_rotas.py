
def test_app_is_created(app):

    ''' Testa se o APP foi criado com sucesso '''

    assert app.name == "backend.cartao"


def test_rota_solicitacao(client):

    ''' testa a rota /solicitacoes '''

    resp = client.get("/solicitacoes")
    assert resp.status_code == 200









