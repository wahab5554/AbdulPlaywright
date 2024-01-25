from playwright.sync_api import expect
import re
from pytest_bdd import *








def test_has_title(page,browser_type):
    browser = browser_type.launch(headless=True, slow_mo=6000)
    page = browser.new_page()
    page.goto("https://playwright.dev/")


    page.title()


    assert page.title()=='Fast and reliable end-to-end testing for modern web apps | Playwright'