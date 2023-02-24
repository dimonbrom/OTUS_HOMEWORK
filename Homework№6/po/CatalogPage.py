from selenium.webdriver.remote.webelement import WebElement
from BasePage import *


class CatalogPage(BasePage):
    CATALOG = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs', 'Cameras',
               'MP3 Players']
    TYPE_CAMERAS = "[title='Nikon D300']"
