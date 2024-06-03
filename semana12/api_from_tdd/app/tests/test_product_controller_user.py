def test_get_animals_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de animales
    response = test_client.get("/api/animals", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, admin_auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Lion"
    assert response.json["species"] == "Panthera leo"
    assert response.json["age"] == 5


def test_get_animal_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener un animal específico
    # Este test asume que existe al menos un animal en la base de datos
    response = test_client.get("/api/animals/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json


def test_create_animal_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un animal
    data = {"name": "Leopard", "species": "Panthera pardus", "age": 4}
    response = test_client.post("/api/animals", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_update_animal_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un animal
    data = {"name": "Lion", "species": "Panthera leo", "age": 6}
    response = test_client.put("/api/animals/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_animal_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un animal
    response = test_client.delete("/api/animals/1", headers=user_auth_headers)
    assert response.status_code == 403
