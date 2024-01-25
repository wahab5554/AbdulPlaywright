from playwright.sync_api import expect
import re
from pytest_bdd import *







def test_visit_youtube(page,browser_type):
    browser=browser_type.launch(headless=False,slow_mo=6000,executable_path='/path/to/chromium-executable')
    page=browser.new_page()
    page.goto("https://youtube.com")
    browser.close()
    breakpoint()

def test_has_title(page,browser_type):
    browser = browser_type.launch(headless=False, slow_mo=6000)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill("abdul.wahab@spglobal.com")
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("$ecurity@964@")
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_timeout(timeout=5000)

    page.title()


    assert page.title()=='Fast and reliable end-to-end testing for modern web apps | Playwright'