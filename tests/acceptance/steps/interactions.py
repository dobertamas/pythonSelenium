from behave import *
from behave import when

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@when('Admin user enters valid admin credentials')
def step_impl(context):
    page = HomePage(context.driver)
    page.enter_credentials(context)


@when('Admin user clicks on Sign in button')
def step_impl(context):
    page = HomePage(context.driver)
    page.click_sign_in(context)


@when('Admin user clicks on the "Push Queue" link from the pull-down menu')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Admin user clicks on the "Push Queue" link from the pull-down menu')
