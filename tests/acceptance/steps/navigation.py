from behave import *
from selenium import webdriver
from nose.tools import *

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@given('Admin user is on the home page')
def step_impl(context):
    cap = {'binary_location': '/opt/geckodriver'}
    context.driver = webdriver.Chrome(desired_capabilities=cap, executable_path='/opt/geckodriver')

    page = HomePage(context.driver)
    context.driver.get(page.url)


@then('Admin user is on the Global Preferences page')
def step_impl(context):
    expected_url = 'http://localhost:8084/console/config/list'
    # print(expected_url)
    current_url = context.driver.current_url
    # print(current_url)
    # assert context.driver.current_url == expected_url
    assert_equal(current_url, expected_url)
    context.driver.close()

@given('Admin user successfully logged in')
def step_impl(context):
