from unittest import mock

from fastapi.testclient import TestClient
from fastapi_di_sample.app import app
from fastapi_di_sample.my_db_client import IMyDbClient

test_client = TestClient(app)


def test_get():
    request_params = {"word": "bob"}
    response = test_client.get("/", params=request_params)
    assert response.status_code == 200
    assert response.json() == {"is_ok": True}

    request_params = {"word": "!!!"}
    response = test_client.get("/", params=request_params)
    assert response.status_code == 200
    assert response.json() == {"is_ok": False}


def test_get_mock_pass():
    client_mock = mock.MagicMock(spec=IMyDbClient)
    client_mock.get_ok_words.return_value = ["foo", "bar", "baz"]

    with app.container.my_client.override(client_mock):
        request_params = {"word": "bar"}
        response = test_client.get("/", params=request_params)
        assert response.status_code == 200
        assert response.json() == {"is_ok": True}


def test_get_mock_fail():
    client_mock = mock.MagicMock(spec=IMyDbClient)
    client_mock.get_ok_words.return_value = ["taro", "jiro", "saburo"]

    with app.container.my_client.override(client_mock):
        request_params = {"word": "alice"}
        response = test_client.get("/", params=request_params)
        assert response.status_code == 200
        assert response.json() == {"is_ok": False}
