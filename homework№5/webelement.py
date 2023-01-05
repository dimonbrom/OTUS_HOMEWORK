import time

from conftest import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def test_webelement(browser):
    browser.get(browser.base_url)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-block.btn-lg')
    print(btn.get_attribute('class'))
    print(btn.tag_name)
    print(btn.size)
    print(btn.location)
    print(btn.rect)
    inp = browser.find_element(By.CSS_SELECTOR, "[name='search']")
    inp.send_keys('1234567')
    inp.send_keys(Keys.BACK_SPACE)
   # browser.save_screenshot('inp.png')
    inp.send_keys(Keys.ARROW_LEFT)
    inp.send_keys(Keys.ARROW_LEFT)
    inp.send_keys(Keys.ARROW_LEFT)
    inp.send_keys(Keys.SPACE)
    inp.send_keys(u'\u2764')
    #inp.screenshot('test_element.png')
    disp = inp.is_displayed()  # для проверки виден ли эмелемен пользователю
    inp.clear()
    tst = browser.find_element(By.XPATH, "//*[text()='Desktops']")
    actions = ActionChains(browser)
    ''' 
    нажать кнопку мыши на элементе и 
       зажать, далее пауза в 1 секунду, далее видем к мышь к другому элменту, далее отпускаем мышь,перформ нужна чтобы 
       все действия были видны пользователю
    '''
    actions.click_and_hold(tst).pause(1).move_to_element(inp).release().perform()

