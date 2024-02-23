from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI
from pytest_bdd.parsers import parse
obj_playwright_api = PlaywrightAPI()


@scenario('validate_kinnarps_api.feature',
          'Verify Kinnarps page load end points')
def test_validate_kinnarps_api():
    """Validate API end point"""


@given('User is login to the kinnarps platform')
def login():
    obj_playwright_api.login()


@then(parse('I must see success response from {endpoints}'),converters=dict(endpoints=str))
def validate_response(endpoints):

    obj_playwright_api.validate_request(endpoints)
