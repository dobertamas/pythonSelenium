from tests.acceptance.locators.home_page import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.url = 'http://localhost:8084/console/login'
        self.driver = driver

        @property
        def url(self):
            return 'http://localhost:8084/console'

        def title(self):
            return self.driver.find_element(*HomePageLocators.TITLE)
