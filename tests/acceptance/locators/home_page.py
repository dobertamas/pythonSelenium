from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


# noinspection SpellCheckingInspection
class HomePageLocators(BasePageLocators):
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'signin')
