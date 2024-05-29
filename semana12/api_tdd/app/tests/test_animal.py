def test_get_animals(test_client):
    response = test_client.get("/api/animals")
    assert response.status_code == 401
    # Dependiendo de tu implementación, ajusta el contenido esperado
    # assert b"animal data" in response.data


def test_post_animal(test_client):
    new_animal = {"name": "Lion", "species": "Panthera leo"}
    response = test_client.post("/api/animals", json=new_animal)
    assert response.status_code == 401
    # Comprueba que el animal ha sido añadido correctamente
    # assert b"Lion" in response.data
