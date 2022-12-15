from app import create_app


def test_index():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert  b"Hello World!" in response.data


def test_alphabet_check():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        # 405 method not allowed for GET
        response = test_client.get('/alphabet-check')
        assert response.status_code == 405
        # Check falsy input returns 200 false
        response = test_client.post('/alphabet-check', json="abc")
        assert response.status_code == 200
        assert response.json is False
        # Check truthy input returns 200 true
        response = test_client.post('/alphabet-check', json="abcdefghijklmnopqrstuvwxyz")
        assert response.status_code == 200
        assert response.json is True
