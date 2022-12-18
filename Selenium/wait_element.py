import random

from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_check_elements(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    WebDriverWait(browser, 11).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".box")))
    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))


#можно через константную велечину
def test_check_title(browser):
    browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
    wait = WebDriverWait(browser, 15)
    wait.until(EC.title_is("Loaded!"))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content"), "This is else page content."))
    el = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert el.text == "This is else page content."

"""Теперь создадим собственное ожидание"""
def amount_of_elements(selector, amount):

    def __predicate(driver):
        #Ищем все элементы на странице
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        #Ecли кол-во элементов совпало с ожиданием
        if len(elements) == amount:
        #Если ожидание некое кол-во элементов (1 или больше) или же если ожидаем именно 0
            if amount == 0:
                return True
            return elements if amount > 1 else elements[0]
        # Иначе возвращаем сразу false если кол-во элементов не совпало с ожиданием
        else:
            return False
    return __predicate


def test_check_magic_button(browser):
    browser.get("https://konflic.github.io/examples/pages/ajax.html")
    button = browser.find_element(By.NAME, "showjsbutton")
    #задаем произвольное кол-во кликов
    test_amount = random.randint(3, 8)
    for i in range(test_amount):
        button.click()
    #Ждем пока не появится нужное количество элементов
    elements = WebDriverWait(browser, 10).until(amount_of_elements(".target", test_amount))
    #Выполняем клик по всем кроме 1 элемента
    elements.pop()
    for el in elements:
        el.click()
    #Ждем пока останется 1 элемент на странице
    last_element = WebDriverWait(browser, 7).until(amount_of_elements('.target', 1))
    last_element.click()
    #Ждем пока не останется элементов на странице
    WebDriverWait(browser, 7).until(amount_of_elements('.target', 0))

