from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocator


class HomePageLocators(BasePageLocator):
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'signin')

