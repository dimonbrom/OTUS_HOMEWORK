from conftest import *
from locator import *
import time


def test_home_page(browser):
    browser.get(browser.base_url)
    """Проверяем текстовку вкладки"""
    WebDriverWait(browser, 2).until(EC.title_is('Your Store'))
    """Ожидаем появления второго слайда"""
    wait_elements(browser=browser, selector=slide_second, time=4, wait_type=EC.visibility_of_element_located)
    """Убеждаемся, что на странице отсутствует подсказка о небходимости авторизации"""
    wait_elements(browser=browser, selector=authorization_prompt, time=4, wait_type=EC.invisibility_of_element_located)
    """Ожидаем появления определенной картинки"""
    browser.execute_script("window.scrollTo(0, 1080)")
    wait_elements(browser=browser, selector=image_Sony, time=27, wait_type=EC.visibility_of_element_located)
    """Добавляем товар в избранные"""
    browser.find_element(By.CSS_SELECTOR, add_l).click()
    """Убеждаемся что появилось предупреждение об авторизации"""
    wait_elements(browser=browser, selector=authorization_prompt, time=27,
                  wait_type=EC.visibility_of_any_elements_located)
    """Проверяем что в избрынных появился 1 товар"""
    WList = browser.find_element(By.CSS_SELECTOR, my_list)
    assert WList.text == "Wish List (1)"


def test_catalog_page(browser):
    browser.get(browser.base_url)
    """Заходим в раздел Камеры и проверяем наличие всех разделов в верт.списке каталога"""
    browser.find_element(By.XPATH, cameras).click()
    all_products = wait_elements(browser=browser, selector=group_list, time=3,
                                 wait_type=EC.visibility_of_all_elements_located)
    sections = ','.join(catalog)
    text_all_products = ','.join([i.text for i in all_products])
    for sections in text_all_products:
        assert True


@pytest.mark.parametrize('messanger', select_loc)
def test_page_cart_product(browser, messanger):
    browser.get(browser.base_url + '/camera/nikon-d300')
    """Проверяем текстовку вкладки"""
    Share = browser.find_element(By.CSS_SELECTOR, dropdown_list)
    browser.execute_script("window.scrollTo(0, 540)")
    ActionChains(browser).move_to_element(Share).perform()
    wait_elements(browser=browser, time=30, selector=f"#atic_{messanger}", wait_type=EC.visibility_of_element_located)


def test_page_admin(browser):
    browser.get(browser.base_url + '/admin')
    """Проверям наличие инструкции"""
    el = wait_elements(browser=browser, time=2, selector=header_admin, wait_type=EC.visibility_of_element_located)
    assert el.text == 'Please enter your login details.'
    """Проверям отсутствие ошибки авторизации"""
    wait_elements(browser=browser, time=3, selector=invalid_data, wait_type=EC.invisibility_of_element_located)
    """Вводим логин и нажимаем кнопку"""
    browser.find_element(By.CSS_SELECTOR, locator_username).send_keys(username)
    browser.find_element(By.CSS_SELECTOR, button_next).click()
    """Проверям наличие ошибки о логине/пароле"""
    alert = wait_elements(browser=browser, time=2, selector=invalid_data, wait_type=EC.visibility_of_element_located)
    assert alert.text == 'No match for Username and/or Password.\n×'
    """нажимаем восстановить пароль и проверяем наличие ошибки"""
    browser.find_element(By.XPATH, "//*[text()='Forgotten Password']").click()
    wait_elements(browser=browser, time=2, selector=reset_on_emeil,
                  wait_type=EC.visibility_of_element_located).send_keys(username)
    browser.find_element(By.CSS_SELECTOR, button_next).click()
    alert = wait_elements(browser=browser, time=2, selector=invalid_data, wait_type=EC.visibility_of_element_located)
    assert alert.text == 'Warning: The E-Mail Address was not found in our records, please try again!\n×'


def test_page_registration(browser):
    browser.get(browser.base_url + '/index.php?route=account/register')
    all_field = wait_elements(browser=browser, time=2, selector=page_registrator,
                              wait_type=EC.visibility_of_all_elements_located)
    text_all_field = ','.join([i.text for i in all_field])
    i_field = ','.join([i for i in list_field])
    for i_field in text_all_field:
        assert True
