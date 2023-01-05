import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        '--browser', default='chrome', help='browser to run tests'
    )

    parser.addoption(
        '--headless', action='store_true', help='running tests without a browser'
    )

    parser.addoption(
        '--directory', default='C:\driver', help='select directory'
    )

    parser.addoption(
        '--Url', default='http://192.168.0.19:8081', help='base url'
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    directory = request.config.getoption('--directory')
    base_url = request.config.getoption('--Url')
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.headless = True
        _driver = webdriver.Chrome(executable_path=f'{directory}\chromedriver.exe', options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.headless = True
        firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        _driver = webdriver.Firefox(executable_path=f'{directory}\geckodriver.exe', options=firefox_options)
    elif browser_name == 'yandex':
        yandex_options = ChromeOptions()
        if headless:
            yandex_options.headless = True
        binary_yandex_driver_file = f'{directory}\yandexdriver.exe'
        _driver = webdriver.Chrome(binary_yandex_driver_file, options=yandex_options)
    else:
        raise ValueError(f'this browser {browser_name} is not supported')
    _driver.base_url = base_url
    _driver.maximize_window()
    yield _driver
    _driver.close()
