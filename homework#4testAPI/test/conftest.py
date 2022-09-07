import json
import pytest
import requests

URL_dogs = 'https://dog.ceo/api'
URL_brewery = 'https://api.openbrewerydb.org/breweries'
URL_json = 'https://jsonplaceholder.typicode.com'


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru/",)
    parser.addoption("--status_code", default=200,)

@pytest.fixture()
def some_url(request):
    return request.config.getoption("--url")

@pytest.fixture()
def status_code(request):
    return request.config.getoption("--status_code")














