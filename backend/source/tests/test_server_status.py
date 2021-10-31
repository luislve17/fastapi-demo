from .utils import get_endpoint, consume_endpoint

def test_endpoint_path():
    expected_path = 'server-status/'
    current_path = get_endpoint("server_status")
    assert current_path == expected_path

def test_response_msg():
    response = consume_endpoint('server_status')
    data = response.json()
    assert len(data) == 1
    for key, val in data.items():
        assert key == "endpoint_name"
        assert val == "server-status"

def test_server_temperature_labels():
    expected_temperature_labels = ["hot", "cold", "unavailable"]
    response = consume_endpoint('server_temperature')
    for _, temperature in response.json().items():
        assert temperature in expected_temperature_labels