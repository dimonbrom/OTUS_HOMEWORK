import random

from BasePage import *


class RegPage(BasePage):
    REGISTER_PATH = '/index.php?route=account/register'
    LIST_FIELD = ['First Name\n', 'Last Name\n', 'E-mail\n', 'nTelephone\n', 'nPassword\n', 'nPassword Confirm\n']
    PRIVACY_POLICY = "[type='checkbox']"
    CONTINUE = "[value='Continue']"
    value_field = ['test1@mail.ru', 'test2@mail.ru', 'test3@mail.ru', 'test4@mail.ru', 'test5@mail.ru',
                   'test6@mail.ru', 'test7@mail.ru', 'test8@mail.ru', 'test9@mail.ru', 'test1@mail.ru']
    FINISH_REG = 'H1'
    page_registrator = '.form-horizontal'

    def random_user(self):
        return random.choice(RegPage.value_field)

    def fill_fields(self, field, value, sel_keys):
        EL = BasePage(self.driver).element(By.CSS_SELECTOR, f".required.form-group .col-sm-10 [name={field}]")
        actions = ActionChains(self.driver)
        actions.click(EL).send_keys(value).send_keys(sel_keys).perform()

    def finish_check(self):
        if BasePage(self.driver).element(By.CSS_SELECTOR, RegPage.FINISH_REG).text == 'Your Account Has Been Created!':
            BasePage(self.driver).element(By.CSS_SELECTOR, BasePage.MY_ACCOUNT).click()
            BasePage(self.driver).element(By.XPATH, BasePage.LOGOUT).click()
        else:
            BasePage(self.driver).fing_alert('Warning: E-Mail Address is already registered!')
