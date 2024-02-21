import json

import playwright.async_api
from playwright.sync_api import sync_playwright,Playwright

from features.Config.configmanager import ConfigurationManager


class PlaywrightAPI:
    def __init__(self):
        self.response = None
        self.auth_token=None
        self.playwright = sync_playwright().start()

        self.config = ConfigurationManager()
        self.current_exec = self.config.obj_config['execution']['current_exec']
        self.current_module = self.config.obj_config['execution']['current_module']
        self.base_url = self.config.obj_config[self.current_exec][self.current_module]['login_api']
        self.user = self.config.obj_config[self.current_exec][self.current_module]['user']
        self.pwd = self.config.obj_config[self.current_exec][self.current_module]['pwd']


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


            user_data={"Username":self.user,"Password":self.pwd}
            context = self.playwright.request.new_context().post(url=self.base_url,data=user_data)
            self.response = context.text()
            if self.current_module=='kinnarps':
                self.auth_token = json.loads(self.response)['result']['token']
            else:
                self.auth_token=json.loads(self.response)['access_token']
        except Exception as e:
            print("An error occurred:", str(e))
    def validate_job_status(self,url):
        try:
            headers={
                'Authorization':'Bearer '+self.auth_token}
            context = self.playwright.request.new_context().get(url='https://qa-bk-api.cubivue.com/api/Job/GetJobsStatusCounts?diomNr=null',
                                                                 headers=headers)
            assert context.ok
        except Exception as e:
            print("An error occurred:", str(e))