from app import app

def test_get_users():
    client = app.test_client()

    response = client.get("/users")

    assert response.status_code == 200


def test_get_user():
    client = app.test_client()

    response = client.get("/users/1")

    assert response.status_code == 200


def test_user_not_found():
    client = app.test_client()

    response = client.get("/users/999")

    assert response.status_code == 404
