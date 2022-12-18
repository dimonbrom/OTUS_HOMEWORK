from conftest import *


def test_hello_selenium(browser):
    browser.get(url=browser.base_url)
    assert browser.title =='Your Store'


