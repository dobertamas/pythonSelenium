from selenium.webdriver.common.by import By


class HomePageLocators:
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'signin')

