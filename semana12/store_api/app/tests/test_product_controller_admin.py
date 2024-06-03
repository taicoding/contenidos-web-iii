import pytest

# Tests para el controlador de productos


def test_get_products(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener la lista de productos
    response = test_client.get("/api/products", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto
    data = {
        "name": "Smartphone",
        "description": "Powerful smartphone with advanced features",
        "price": 599.99,
        "stock": 100,
    }
    response = test_client.post("/api/products", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Smartphone"
    assert response.json["description"] == "Powerful smartphone with advanced features"
    assert response.json["price"] == 599.99
    assert response.json["stock"] == 100


def test_get_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/products/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json


def test_get_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar obtener un producto inexistente
    response = test_client.get("/api/products/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_create_product_invalid_data(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar crear un producto sin datos requeridos
    data = {"name": "Laptop"}  # Falta description, price y stock
    response = test_client.post("/api/products", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder actualizar un producto existente
    data = {
        "name": "Smartphone Pro",
        "description": "Updated version with improved performance",
        "price": 699.99,
        "stock": 150,
    }
    response = test_client.put("/api/products/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Smartphone Pro"
    assert response.json["description"] == "Updated version with improved performance"
    assert response.json["price"] == 699.99
    assert response.json["stock"] == 150


def test_update_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar actualizar un producto inexistente
    data = {
        "name": "Tablet",
        "description": "Portable device with touchscreen interface",
        "price": 299.99,
        "stock": 50,
    }
    response = test_client.put(
        "/api/products/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_delete_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder eliminar un producto existente
    response = test_client.delete("/api/products/1", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el producto ha sido eliminado
    response = test_client.get("/api/products/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"


def test_delete_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar eliminar un producto inexistente
    response = test_client.delete("/api/products/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Producto no encontrado"
