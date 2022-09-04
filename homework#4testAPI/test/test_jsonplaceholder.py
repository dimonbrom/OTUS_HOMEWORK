from test_data import *
from conftest import *


@pytest.mark.parametrize('value3, value1, value2', [
    (201, 'some text0', 'test1'),
    (207, 'some text1', 'test2'),
    (211, 'some text2', 'test3'),
    (304, 'some text3', 'test4'),
    (314, 'some text4', 'test5'),
])
def test_creating_resourse(value3, value1, value2):
    response = requests.post(URL_json + '/posts', headers={'Content-type': 'application/json; charset=UTF-8'},
                             json={'title': value1, 'body': value2, 'userId': value3, })
    assert response.json() == {'title': value1, 'body': value2, 'userId': value3, 'id': 101}


@pytest.mark.parametrize('id', [1, 44, 57, 68])
def test_getting_resourse(id):
    response = requests.get(URL_json + f'/posts/{id}')
    assert response.json()['userId'] in user_json


@pytest.mark.parametrize('id', id_json)
def test_patching_resource(id):
    response = requests.patch(URL_json + f'/posts/{id}',
                              headers={'Content-type': 'application/json; charset=UTF-8'},
                              json={'title': 'update autotest'})
    assert response.status_code == 200


def test_filtering_resources():
    response = requests.get(URL_json + '/posts', params={'userId': 4})
    assert len(response.json()) == 10


@pytest.mark.parametrize('val', [2, 4, 7])
def test_update_resources(val):
    response = requests.put(URL_json + f'/posts/{val}',
                            json={'id': val, 'title': 'foo', 'body': 'bar', 'userId': 666},
                            headers={'Content-type': 'application/json; charset=UTF-8'})
    assert response.json() == {'title': 'foo', 'body': 'bar', 'userId': 666, 'id': val}
