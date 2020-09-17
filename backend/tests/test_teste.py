
def test_app_is_created(app):

    ''' Testa se o APP foi criado com sucesso '''

    assert app.name == "backend.cartao"

def test_raiz(client):

    ''' testa a rota / '''

    resp = client.get("/")
    assert resp.status_code == 200







