from app import app


def test_sum_api():

    client = app.test_client()

    response = client.post(
        "/sum",
        json={
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 15


def test_missing_parameter():

    client = app.test_client()

    response = client.post(
        "/sum",
        json={
            "a": 10
        }
    )

    assert response.status_code == 400
