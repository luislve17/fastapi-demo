from .utils import get_endpoint, consume_endpoint

def test_endpoint_path():
    expected_path = 'hello-world/'
    current_path = get_endpoint("hello_world")
    assert current_path == expected_path

def test_helloworld_msg():
    hello_world_response = consume_endpoint('hello_world')
    hello_world_data = hello_world_response.json()
    assert len(hello_world_data) == 1
    for key, val in hello_world_data.items():
        assert key == "Hello"
        assert val == "World"