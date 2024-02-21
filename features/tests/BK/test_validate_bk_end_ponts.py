from pytest_bdd import *
from features.services.playwright_api import PlaywrightAPI

obj_playwright_api = PlaywrightAPI()


@scenario('validate_bk_end_points.feature',
          'Verify Get Job Status endpoint')
def test_validate_bk_api():
    """Validate API end point"""


@given('I login to BK platorm')
def login():
    obj_playwright_api.login()


@then('I must see success response in job status')
def validate_response():
    url = 'https://qa-bk-api.cubivue.com/api/Job/GetJobsStatusCounts?diomNr=null'
    obj_playwright_api.validate_job_status(url)
