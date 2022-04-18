'''api_test.py'''

def test_hello_endpoint(test_client):
    response = test_client.get("/");
    assert response.status_code == 200
    assert b'hello world' in response.data