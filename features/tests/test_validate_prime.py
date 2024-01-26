from pytest_bdd import *
from features.forms.playwrightui import PlaywrightUI
obj_playwrightui=PlaywrightUI(browser_type="firefox")



@scenario('UI/Validate_prime.feature',
          'Verify user is able to create dataset')
def test_verify_prime():
    """Verify user is able to create dataset"""
@scenario('UI/Validate_prime.feature',
          'Verify title for playwright')
def test_verify_playwright():
    """Verify title for playwright"""
@given('User is login to the prime platform')
def user_login():

    obj_playwrightui.navigate_url("https://playwright.dev/")

@when('User lands on <url>')
def navigate_url(url):

    obj_playwrightui.navigate_url(url)


@then('User must see {title}')
def validate(title):
    obj_playwrightui.validate_page_title(title)

@when('User navigates to Dataset menu option')
def user_navigate():
    pass
