
from playwright.sync_api import sync_playwright
from features.Config.configmanager import ConfigurationManager

class PlaywrightUI:
    def __init__(self):
        self.page = None
        self.config = ConfigurationManager()
        self.browser_type = self.config.obj_config['execution']['browser']


    def navigate_url(self, url):
        with sync_playwright() as p:
            browser = p[self.browser_type].launch(headless=False, slow_mo=6000)
            self.page = browser.new_page()
            self.page.goto(url)

    def validate_page_title(self, pstr_title):
        assert self.page.title() == pstr_title