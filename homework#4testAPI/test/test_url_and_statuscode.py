from conftest import *


def test_status_code_validity_for_address(some_url, status_code):
    response = requests.get(f'{some_url}')
    assert response.status_code == int(status_code)
