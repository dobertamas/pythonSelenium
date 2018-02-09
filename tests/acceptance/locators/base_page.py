from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = (By.TAG_NAME, 'title')
    NAV_LINKS = (By.CLASS_NAME, 'dropdown-toggle')
