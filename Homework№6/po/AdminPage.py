from BasePage import *


class AdminPage(BasePage):
    ADMIN_PATH = '/admin'
    HEADER_ADM = '.panel-heading'
    LOCATOR_USNAME = "[name='username']"
    LOCATOR_PASSW = "[name='password']"
    USERNAME = 'user'
    PASSWORD = 'bitnami'
    LOGIN_BTN = '.btn'
    RESTART_PASSWORD = "//*[text()='Forgotten Password']"
    RESET_ON_EMAIL = '#input-email'
    ADD_NEW = "[data-original-title = 'Add New']"
    FILTER_BNT = "[id='button-filter']"
    CHECKBOX_FILTER_TABLE = "[type = 'checkbox']"
    DELETE_BTN = "[data-original-title='Delete']"

    def log_admin(self):
        BasePage(self.driver).open(AdminPage.ADMIN_PATH)
        BasePage(self.driver).element(By.CSS_SELECTOR, AdminPage.LOCATOR_USNAME).send_keys(AdminPage.USERNAME)
        BasePage(self.driver).element(By.CSS_SELECTOR, AdminPage.LOCATOR_PASSW).send_keys(AdminPage.PASSWORD)
        BasePage(self.driver).element(By.CSS_SELECTOR, AdminPage.LOGIN_BTN).click()

    def select_menu_admin(self, type_menu, number_form):
        BasePage(self.driver).element(By.CSS_SELECTOR, f'#menu-{type_menu}').click()
        BasePage(self.driver).wait_elements(f'#collapse1 > li:nth-child({number_form})', 5,
                                            EC.visibility_of_element_located).click()

    def fill_fields_to_create(self, field_for_create, number_form, tool):
        field = BasePage(self.driver).wait_elements(f".form-group .col-sm-10 [placeholder = '{field_for_create}']", 3,
                                                    EC.visibility_of_element_located)
        select_tools = BasePage(self.driver).element(By.XPATH, f"//*[text()='{tool}']")
        actions = ActionChains(self.driver)
        actions.click(field).send_keys(number_form).click(select_tools).perform()

    def find_by_filter(self,  method, product):
        """available filter - name, model, price"""
        BasePage(self.driver).element(By.CSS_SELECTOR, f"[id='input-{method}']").send_keys(product)
        BasePage(self.driver).element(By.CSS_SELECTOR, AdminPage.FILTER_BNT).click()
        result_seurch = BasePage(self.driver).wait_elements('tbody tr .text-left', 2, EC.visibility_of_element_located)
        assert product == result_seurch.text
