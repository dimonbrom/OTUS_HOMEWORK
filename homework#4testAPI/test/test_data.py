import json
import pytest
import requests
from conftest import *


def get_list_dog_response():
    with open("C:/Users/stak-/OTUS_HOMEWORK/homework#4testAPI/message.json", "r") as f:
        responce = json.load(f)
        return responce


excepted = get_list_dog_response()

with open("C:/Users/stak-/OTUS_HOMEWORK/homework#4testAPI/message.json", "r") as f:
    response = json.load(f)

l_dog = [el for el in response['message']]

response = requests.get(URL_brewery)
list_brewery = response.json()
res = [x.get('id') for x in list_brewery]

response = requests.get(URL_json + '/posts')
list_js = response.json()
user_json = [x.get('userId') for x in list_js]
id_json = [x.get('id') for x in list_js]
