def test_get_animals(test_client, admin_auth_headers):
    response = test_client.get("/api/animals", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, admin_auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Lion"
    assert response.json["species"] == "Panthera leo"
    assert response.json["age"] == 5


def test_get_animal(test_client, admin_auth_headers):
    # Primero crea un animal
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"
    assert response.json["species"] == "Panthera tigris"
    assert response.json["age"] == 3


def test_get_nonexistent_animal(test_client, admin_auth_headers):
    response = test_client.get("/api/animals/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Animal no encontrado"


def test_create_animal_invalid_data(test_client, admin_auth_headers):
    data = {"name": "Elephant"}  # Falta species y age
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_animal(test_client, admin_auth_headers):
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["name"] == "Elephant"
    assert response.json["species"] == "Loxodonta africana"
    assert response.json["age"] == 12


def test_update_nonexistent_animal(test_client, admin_auth_headers):
    update_data = {"name": "Rhino", "species": "Rhinocerotidae", "age": 5}
    response = test_client.put(
        "/api/animals/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Animal no encontrado"


def test_delete_animal(test_client, admin_auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(
        f"/api/animals/{animal_id}", headers=admin_auth_headers
    )
    assert response.status_code == 204

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Animal no encontrado"


def test_delete_nonexistent_animal(test_client, admin_auth_headers):
    response = test_client.delete("/api/animals/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Animal no encontrado"
