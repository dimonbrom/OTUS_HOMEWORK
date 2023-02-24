import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class BasePage:
    AUTORIZATION_PROMT = ".alert"
    ADD_TO_WISH_LIST = "[data-original-title='Add to Wish List']"
    MY_LIST = '#wishlist-total .hidden-sm'
    CAMERAS = "//*[text()='Cameras']"
    GROUP_L = ".list-group-item"
    SHARE_L = ['facebook', 'twitter', 'print', 'pinterest_share', 'gmail', 'linkedin', 'more']
    DROPDOWN_LIST = '.atc_s.addthis_button_compact'
    URL = 'http://192.168.0.16:8081'
    HORIZONTAL_FORM = '.form-horizontal'
    CURRENCY_MENU = '.btn-group .hidden-xs'
    CURRENCY_VALUE = '.btn-group button strong'
    LOGOUT = "//*[text()='Logout']"
    MY_ACCOUNT = "[title ='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def wait_elements(self, selector, time, wait_type):
        try:
            return WebDriverWait(self.driver, time).until(wait_type((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise AssertionError(f'явное ожидание {wait_type} не сработало в течении {time} секунд')

    def check_title(self, name_title):
        try:
            return WebDriverWait(self.driver, 2).until(EC.title_is(name_title))
        except TimeoutException:
            raise AssertionError(f'Заголовок {name_title} не прогрузился')

    def use_scroll_on_page(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def element(self, sel, locator):
        try:
            return self.driver.find_element(sel, locator)
        except NoSuchElementException:
            raise AssertionError(f'селектор {locator} на найден на странице')

    def open(self, path):
        self.driver.get(BasePage.URL + path)

    def select_currency(self, val):
        """available currency - EUR, GBR, USD"""
        BasePage(self.driver).element(By.CSS_SELECTOR, BasePage.CURRENCY_MENU).click()
        type_value = BasePage(self.driver).element(By.CSS_SELECTOR, f"li [ name={val}]")
        type_text = type_value.text
        type_value.click()
        current_currency = BasePage(self.driver).element(By.CSS_SELECTOR, BasePage.CURRENCY_VALUE).text
        assert current_currency in type_text

    def fing_alert(self, exp_val):
        al = BasePage(self.driver).wait_elements(BasePage.AUTORIZATION_PROMT, 5, EC.visibility_of_element_located)
        assert al.text == exp_val
        print(al.text)
