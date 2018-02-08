from tests.acceptance.locators.home_page import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        #self.url =''

        @property
        def url(self):
            return 'http://localhost:8084/console'

        def title(self):
            return self.driver.find_element(*HomePageLocators.TITLE)
