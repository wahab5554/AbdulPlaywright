from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI
obj_playwright_api=PlaywrightAPI()



@scenario('api_test.feature',
          'Validate API end point')
def test_api():
    """Validate API end point"""



@when('I go to google page')
def navigate_url():

    obj_playwright_api.reques_build("https://www.google.com/")


@then('I must see success response')
def validate_response():
    obj_playwright_api.validate_response()

