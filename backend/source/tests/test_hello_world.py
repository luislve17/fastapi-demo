from .utils import get_endpoint

def test_endpoint_path():
    expected_path = 'hello-world/'
    current_path = get_endpoint("hello_world")
    assert current_path == expected_path