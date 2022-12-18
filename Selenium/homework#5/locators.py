import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

username = 'test@mail.ru'
slide_second = ".swiper-slide-active[data-swiper-slide-index='1']"
authorization_prompt = ".alert"
image_Sony = "[data-swiper-slide-index='2'].swiper-slide-active"
add_l = "[data-original-title='Add to Wish List']"
my_list = '#wishlist-total .hidden-sm'
cameras = "//*[text()='Cameras']"
group_list = ".list-group-item"
catalog = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs', 'Cameras',
              'MP3 Players']
Share_l = ['facebook', 'twitter', 'print', 'pinterest_share', 'gmail', 'linkedin', 'more']
select_loc = [i for i in Share_l]
list_field = ['First Name\n', 'Last Name\n', 'E-mail\n', 'nTelephone\n', 'nPassword\n', 'nPassword Confirm\n']
dropdown_list = '.atc_s.addthis_button_compact'
header_admin = '.panel-heading'
invalid_data = '.alert'
locator_username = "[name='username']"
button_next = '.btn'
reset_on_emeil = '#input-email'
page_registrator = '.form-horizontal'


def wait_elements(browser, selector, time, wait_type):
    try:
        return WebDriverWait(browser, time).until(wait_type((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        raise AssertionError(f'Явное ожидание {wait_type} не сработало в течении {time} секунд')





