def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 404


def test_swagger_ui(test_client):
    response = test_client.get("/api/docs/")
    assert response.status_code == 200
    assert b'id="swagger-ui"' in response.data
