from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):

    def url(self):
        return super().url + '/'

    def enter_credentials(self, context):
        username_field = context.driver.find_element(*HomePageLocators.USERNAME)
        username_field.send_keys('admin')
        password_field = context.driver.find_element(*HomePageLocators.PASSWORD)
        password_field.send_keys('admin')

    def click_sign_in(self, context):
        sign_in_button = context.driver.find_element(*HomePageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()
