import json

import playwright.async_api
from playwright.sync_api import sync_playwright,Playwright


class PlaywrightAPI:
    def __init__(self):
        self.response = None
        self.auth_token=None
        self.playwright = sync_playwright().start()


    def request_build(self, url):
        try:

            context=self.playwright.request.new_context().get(url=url)
            self.response=context
        except Exception as e:
            print("An error occurred:", str(e))
    def validate_response(self):
        assert self.response.ok
    def login(self):
        try:


            user_data={"Username":"hs","Password":"1234"}
            context = self.playwright.request.new_context().post(url='https://qa-bk-api.cubivue.com/api/Account/Login',data=user_data)
            self.response = context.text()
            self.auth_token=json.loads(self.response)['access_token']
        except Exception as e:
            print("An error occurred:", str(e))
    def validate_job_status(self):
        try:
            headers={
                'Authorization':'Bearer '+self.auth_token}
            context = self.playwright.request.new_context().get(url='https://qa-bk-api.cubivue.com/api/Job/GetJobsStatusCounts?diomNr=null',
                                                                 headers=headers)
            assert context.ok
        except Exception as e:
            print("An error occurred:", str(e))