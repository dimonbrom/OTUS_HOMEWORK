from conftest import *
from test_data import *


def test_list_dog():
    response = requests.get(URL_dogs + '/breeds/list/all')
    assert response.json() == excepted


@pytest.mark.parametrize("breeds", l_dog)
def test_breeds_list(breeds):
    response = requests.get(URL_dogs + f'/breed/{breeds}/images/random')
    assert response.status_code == 200


@pytest.mark.parametrize("data", [2, 34, 50])
def test_multiple_random_images_positive(data):
    response = requests.get(URL_dogs + f'/breeds/image/random/{data}')
    assert len(response.json()["message"]) == data


@pytest.mark.parametrize("data, exp", [
    ((-1), 1),
    ((0), 1),
    ((51), 50),
    ((153), 50)
])
def test_multiple_random_images_negative(data, exp):
    response = requests.get(URL_dogs + f'/breeds/image/random/{data}')
    assert len(response.json()["message"]) == exp


@pytest.mark.parametrize("breeds", l_dog)
def test_random_image_is_in_the_list_of_images_all_breeds(breeds):
    link1 = URL_dogs + f'/breed/{breeds}/images'
    response1 = requests.get(link1)
    val1 = response1.json()
    link2 = URL_dogs + f'/breed/{breeds}/images/random'
    response2 = requests.get(link2)
    val2 = response2.json()
    for val2['message'] in val1['message']:
        assert True


def test_random_breed_and_random_image():
    response = requests.get(URL_dogs + '/breeds/image/random')
    assert response.json()['status'] == "success"
