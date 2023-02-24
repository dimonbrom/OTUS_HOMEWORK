import time

from conftest import *
from HomePage import *
from CatalogPage import *
from ProductPage import *
from AdminPage import *
from RegPage import *
from selenium.webdriver import ActionChains


def test_home_page(browser):
    """Проверяем текстовку вкладки"""
    BasePage(browser).check_title('Your Store')
    """Ожидаем появления второго слайда"""
    BasePage(browser).wait_elements(HomePage.SLIDE_SECOND, 4, EC.visibility_of_element_located)
    """Ожидаем появления определенной картинки"""
    BasePage(browser).use_scroll_on_page(0, 1080)
    BasePage(browser).wait_elements(HomePage.IMAGE_SONY, 27, EC.visibility_of_element_located)
    """Добавляем товар в избранные"""
    BasePage(browser).element(By.CSS_SELECTOR, BasePage.ADD_TO_WISH_LIST).click()
    """Убеждаемся что появилось предупреждение об авторизации"""
    BasePage(browser).wait_elements(HomePage.AUTORIZATION_PROMT, 27, EC.visibility_of_any_elements_located)
    """Проверяем что в избрынных появился 1 товар"""
    WList = BasePage(browser).element(By.CSS_SELECTOR, BasePage.MY_LIST)
    assert WList.text == "Wish List (1)"


def test_catalog_page(browser):
    """Заходим в раздел Камеры и проверяем наличие всех разделов в верт.списке каталога"""
    BasePage(browser).element(By.XPATH, BasePage.CAMERAS).click()
    all_products = BasePage(browser).wait_elements(BasePage.GROUP_L, 3, EC.visibility_of_all_elements_located)
    sections = ','.join(CatalogPage.CATALOG)
    text_all_products = ','.join([i.text for i in all_products])
    for sections in text_all_products:
        assert True


@pytest.mark.parametrize('messanger', ProductPage.SELECT_LOC)
def test_page_cart_product(browser, messanger):
    BasePage(browser).open(ProductPage.PRODUCT_PATH)
    BasePage(browser).use_scroll_on_page(0, 540)
    Share = BasePage(browser).wait_elements(BasePage.DROPDOWN_LIST, 5, EC.visibility_of_element_located)
    ActionChains(browser).move_to_element(Share).perform()
    BasePage(browser).wait_elements(f"#atic_{messanger}", 30, EC.visibility_of_element_located)


def test_page_admin(browser):
    BasePage(browser).open(AdminPage.ADMIN_PATH)
    """Проверям наличие инструкции"""
    el = BasePage(browser).wait_elements(AdminPage.HEADER_ADM, 5, EC.visibility_of_element_located)
    assert el.text == 'Please enter your login details.'
    """Вводим логин и нажимаем кнопку"""
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.LOCATOR_USNAME).send_keys(AdminPage.USERNAME)
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.LOGIN_BTN).click()
    """Проверям наличие ошибки о логине/пароле"""
    BasePage(browser).fing_alert('No match for Username and/or Password.\n×')
    """нажимаем восстановить пароль и проверяем наличие ошибки"""
    BasePage(browser).element(By.XPATH, AdminPage.RESTART_PASSWORD).click()
    BasePage(browser).wait_elements(AdminPage.RESET_ON_EMAIL, 3, EC.visibility_of_element_located).send_keys(
        AdminPage.USERNAME)
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.LOGIN_BTN).click()
    BasePage(browser).fing_alert('Warning: The E-Mail Address was not found in our records, please try again!\n×')


def test_page_registration(browser):
    BasePage(browser).open(RegPage.REGISTER_PATH)
    all_field = BasePage(browser).wait_elements(RegPage.page_registrator, 4, EC.visibility_of_all_elements_located)
    text_all_field = ','.join([i.text for i in all_field])
    i_field = ','.join([i for i in RegPage.LIST_FIELD])
    for i_field in text_all_field:
        assert True


def test_select_currency(browser):
    BasePage(browser).select_currency('USD')


def test_check_registration(browser):
    """Заполняем поля регистрации"""
    BasePage(browser).open(RegPage.REGISTER_PATH)
    RegPage(browser).fill_fields('firstname', RegPage.random_user(browser), Keys.TAB)
    RegPage(browser).fill_fields('lastname', RegPage.random_user(browser), Keys.TAB)
    RegPage(browser).fill_fields('email', RegPage.random_user(browser), Keys.TAB)
    RegPage(browser).fill_fields('telephone', RegPage.random_user(browser), Keys.TAB)
    RegPage(browser).fill_fields('password', '1234', Keys.TAB)
    RegPage(browser).fill_fields('confirm', '1234', Keys.TAB)
    """Нажимаем продолжить и убеждаемся в наличии алерта"""
    BasePage(browser).element(By.CSS_SELECTOR, RegPage.CONTINUE).click()
    BasePage(browser).fing_alert('Warning: You must agree to the Privacy Policy!')
    """Проставляем политику конфедециальности и нажимаем кнопку продолжить"""
    BasePage(browser).element(By.CSS_SELECTOR, RegPage.PRIVACY_POLICY).click()
    BasePage(browser).element(By.CSS_SELECTOR, RegPage.CONTINUE).click()
    """В зависимости от кейса: если регистрация успешна - убеждаемся в корректности текстови, 
       если такой емайл уже занят - убеждаемся в наличии алерта """
    RegPage(browser).finish_check()


def test_create_new_product(browser):
    AdminPage(browser).log_admin()
    AdminPage(browser).select_menu_admin('catalog', 2)
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.ADD_NEW).click()
    AdminPage(browser).fill_fields_to_create('Product Name', 'Test PC', 'General')
    AdminPage(browser).fill_fields_to_create('Meta Tag Title', 'laptop', 'Data')
    AdminPage(browser).fill_fields_to_create('Model', 'HP', 'Data')
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.LOGIN_BTN).click()
    AdminPage(browser).find_by_filter('name', 'Test PC')


def test_delete_new_product(browser):
    AdminPage(browser).log_admin()
    AdminPage(browser).select_menu_admin('catalog', 2)
    AdminPage(browser).find_by_filter('name', 'Test PC')
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.CHECKBOX_FILTER_TABLE).click()
    BasePage(browser).element(By.CSS_SELECTOR, AdminPage.DELETE_BTN).click()
    browser.switch_to.alert.accept()
    RESULT_DELETE = BasePage(browser).element(By.CSS_SELECTOR, "[colspan='8']")
    assert RESULT_DELETE.text == 'No results!'
