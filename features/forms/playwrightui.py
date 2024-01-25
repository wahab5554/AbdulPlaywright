
from playwright.sync_api import sync_playwright


class PlaywrightUI:
    def __init__(self, browser_type):
        self.page = None
        self.browser_type = browser_type

    def navigate_url(self, url):
        with sync_playwright() as p:
            browser = p[self.browser_type].launch(headless=False, slow_mo=6000)
            self.page = browser.new_page()
            self.page.goto(url)

