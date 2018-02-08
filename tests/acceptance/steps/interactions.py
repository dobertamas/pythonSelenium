from behave import *
from behave import when

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@when('I enter credentials')
def step_impl(context):
    page = HomePage(context.driver)
    page.enter_credentials(context)


@when('I click on Sign in')
def step_impl(context):
    page = HomePage(context.driver)
    page.click_sign_in(context)
