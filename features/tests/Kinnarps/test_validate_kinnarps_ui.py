from pytest_bdd import *

from pytest_bdd.parsers import parse

from features.tests.BK.test_validate_bk import obj_playwrightui




@scenario('validate_kinnarps_route_plan.feature',
          'Verify Route Plan Page')
def test_validate_kinnarps_route_plan():
    """Validate API end point"""


@given('User is login to the kinnarps platform')
def login():
    obj_playwrightui.login_kinnarp()


@when('I Click on Route Plan bucket')
def click_route_plan():

    obj_playwrightui.click_route_plan()

@then('I must see Route Detail')
def validate_route_detail():

   pass