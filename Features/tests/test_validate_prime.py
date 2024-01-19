from pytest_bdd import *

from Features.Forms.PlaywrightUI import PlaywrightUI

obj_playwrightui=PlaywrightUI(browser_type="firefox")

@scenario('UI/Validate_prime.feature',
          'Verify user is able to create dataset')
def test_verify_prime():
    """Verify user is able to create dataset"""

@given('User is login to the prime platform')
def user_login():

    obj_playwrightui.navigate_url("https://playwright.dev/")
@when('User navigates to Dataset menu option')
def user_navigate():
    pass
