from .utils import get_endpoint, consume_endpoint

def test_endpoint_path():
    expected_path = 'hello-world/'
    current_path = get_endpoint("hello_world")
    assert current_path == expected_path

def test_response_msg():
    response = consume_endpoint('hello_world')
    data = response.json()
    assert len(data) == 1
    for key, val in data.items():
        assert key == "Hello"
        assert val == "World"