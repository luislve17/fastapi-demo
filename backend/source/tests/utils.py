import re
from typing import Optional
from requests.models import Response
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

ENDPOINT_REGEX = r'.*\/(.+)'

def get_endpoint(endpoint_name:str) -> Optional[str]:
    full_url = app.url_path_for(endpoint_name)
    endpoint_regex = re.search(ENDPOINT_REGEX, full_url)
    current_path = endpoint_regex.group(1) if endpoint_regex else None

    return current_path

def consume_endpoint(endpoint_name:str) -> Response:
    response = client.get(app.url_path_for(endpoint_name))
    return response