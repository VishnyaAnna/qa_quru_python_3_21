from pytest_voluptuous import S

from schemas.user import add_user


def test_create_user_ok(reqres_in):
    body = {
        "name": "cherry",
        "job": "leader"
    }
    response = reqres_in.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == "cherry"


def test_create_user_without_job(reqres_in):
    body = {
        "name": "cherry"
    }
    response = reqres_in.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
