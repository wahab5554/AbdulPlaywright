import playwright.async_api
from playwright.sync_api import sync_playwright


class PlaywrightAPI:
    def __init__(self):
        self.response = None




    def reques_build(self, url):
         with sync_playwright() as p:
            context=p.request.new_context().get(url=url)
            self.response=context
    def validate_response(self):
        assert self.response.ok
