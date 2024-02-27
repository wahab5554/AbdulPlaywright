import json
import os

import playwright.async_api
from playwright.sync_api import sync_playwright,Playwright

from features.Config.configmanager import ConfigurationManager


class PlaywrightAPI:
    def __init__(self):
        self.response = None
        self.auth_token=None
        self.playwright = sync_playwright().start()

        self.config = ConfigurationManager()
        self.obj_service_config= self.config.read_base_service_config_file('services.yml')
        self.current_exec = self.config.obj_config['execution']['current_exec']
        self.current_module = self.config.obj_config['execution']['current_module']
        self.base_url = self.config.obj_config[self.current_exec][self.current_module]['base_url']
        self.user = self.config.obj_config[self.current_exec][self.current_module]['user']
        self.pwd = self.config.obj_config[self.current_exec][self.current_module]['pwd']
        self.payload=None
        self.context=None



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
            context = self.playwright.request.new_context().post(url=self.base_url+'/api/Account/Login',data=user_data)
            self.response = context.text()
            if self.current_module=='kinnarps':
                self.auth_token = json.loads(self.response)['result']['token']
            else:
                self.auth_token=json.loads(self.response)['access_token']
        except Exception as e:
            print("An error occurred:", str(e))
    def validate_request(self,pstr_service,**kwargs):
        try:

            self.payload = self.obj_service_config[pstr_service]['payload']
            self.payload = self.get_payload(self.payload)


            self.obj_service_config[pstr_service]
            req_method=self.obj_service_config[pstr_service]['Method']

            req_url= self.base_url+self.obj_service_config[pstr_service]['endpoint']

            headers=self.obj_service_config[pstr_service]['headers']
            headers['Authorization']='Bearer '+self.auth_token
            for key, value in kwargs.items():
                if key == "payload":
                    self.payload = value
                elif key=="filter":
                    req_url=str(req_url).replace("<<bucketid>>",str(value))

            if req_method=="GET":
                self.context = self.playwright.request.new_context().get(url=req_url,
                                                                 headers=headers)
            elif req_method=="POST":

                self.context = self.playwright.request.new_context().post(url=req_url,
                                                                   headers=headers,data=json.dumps(self.payload))

            assert self.context.ok
        except Exception as e:
            print("An error occurred:", str(e))

    def get_payload(self,pstr_payload):
        try:

            current_directory = os.path.dirname(__file__)

            file_path = os.path.join(current_directory+'\\payloads', pstr_payload)

            # Open the JSON file and load its contents
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data

        except Exception as e:
            print("An error occurred:", str(e))
    def modify_payload(self,pint_orderid,pint_bucketid,pstr_service):
        try:

            self.obj_service_config[pstr_service]

            payload = self.obj_service_config[pstr_service]['payload']
            payload = self.get_payload(payload)
            payload['orders'][0]['orderId']=pint_orderid
            payload['bucketId']=pint_bucketid
            return payload



        except Exception as e:
            print("An error occurred:", str(e))

    def modify_payload_bucket(self,pint_bucketid,pstr_service):
        try:

            self.obj_service_config[pstr_service]

            payload = self.obj_service_config[pstr_service]['payload']
            payload = self.get_payload(payload)

            payload['id']=pint_bucketid
            return payload



        except Exception as e:
            print("An error occurred:", str(e))

    def validate_order(self, pint_orderid):
        try:

            if pint_orderid== json.loads(self.context.text())[0]['id']:
             assert True
            else:
             assert False



        except Exception as e:
            print("An error occurred:", str(e))

    def validate_removed_order(self, pint_orderid):
        try:

            if self.context.text()==[]:
                print("Bucket is empty")
                assert True
            else:
                assert False



        except Exception as e:
            print("An error occurred:", str(e))
    def validate_unplanned_orders(self, pint_orderid):
        try:
            resp=json.loads(self.context.text())
            bool_flg=False
            total_rec=len(resp)
            for i in range(0,total_rec):
                if resp[i]['id']==pint_orderid:
                    print("order found in unplanned list of orders")

                    bool_flg= True
                    break
                else:
                    bool_flg= False
            assert bool_flg



        except Exception as e:
            return False
            print("An error occurred:", str(e))