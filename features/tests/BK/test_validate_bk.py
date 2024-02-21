from pytest_bdd import *
from features.forms.playwrightui import PlaywrightUI


obj_playwrightui = PlaywrightUI()


@scenario('validate_bk.feature',
          'Verify dashboard page for BK')
def test_verify_bk():
    """Verify dashboard page for BK"""



@given('User is login to the bk platform')
def user_login():
    obj_playwrightui.login()


@when('User lands on main page')
def user_lands_main_page():
    obj_playwrightui.validate_dashboard_page()


@then('User must see total jobs section')
def validate_jobs_section():
    pass


