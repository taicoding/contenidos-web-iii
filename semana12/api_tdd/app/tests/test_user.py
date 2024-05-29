def test_register_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201
    # Comprueba que el usuario ha sido añadido correctamente
    # assert b"testuser" in response.data


def test_login_user(test_client):
    user_credentials = {"username": "testuser", "password": "testpassword"}
    response = test_client.post("/api/login", json=user_credentials)
    assert response.status_code == 200
    # Comprueba que el token JWT se devuelve
    # assert b"access_token" in response.data
