from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI

obj_playwright_api = PlaywrightAPI()


@scenario('validate_kinnarps_api.feature',
          'Verify Kinnarps page load end points')
def test_validate_kinnarps_api():
    """Validate API end point"""


@given('User is login to the kinnarps platform')
def login():
    obj_playwright_api.login()


@then('I must see success response in job status')
def validate_response():
    url='https://tptest-api.kinnarps.com/api/Metadata/GetCountries'
    obj_playwright_api.validate_job_status(url)
