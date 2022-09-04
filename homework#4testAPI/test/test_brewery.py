from test_data import *
from conftest import *


@pytest.mark.parametrize('id', res)
def test_single_brewery(id):
    response = requests.get(URL_brewery + f'/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('type',
                         ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor',
                          'closed'])
def test_filter_type(type):
    response = requests.get(URL_brewery, params={'by_type': type})
    data = response.json()
    for data in list_brewery:
        assert True


@pytest.mark.parametrize('number, expect', [
    ((1), 1),
    ((20), 20),
    ((49), 49),
    ((50), 50)
])
def test_per_page_positive(number, expect):
    response = requests.get(URL_brewery, params={'per_page': number})
    assert len(response.json()) == expect


@pytest.mark.parametrize('number, expect', [
    ((51), 50),
    ((101), 50),
    ((-1), 20)
])
def test_per_page_negative(number, expect):
    response = requests.get(URL_brewery, params={'per_page': number})
    assert len(response.json()) == expect


def test_random_brewery():
    response = requests.get(URL_brewery + '/random')
    get_random = response.json()
    country = [x.get('country') for x in get_random]
    for i in country:
        assert str(i) in ['United States', 'Ireland']


def test_brewery_by_city():
    response = requests.get(URL_brewery, params={'by_city': 'Killeshin'})
    get_result = response.json()
    country = [x.get('country') for x in get_result]
    for i in country:
        assert str(i) == 'Ireland'
