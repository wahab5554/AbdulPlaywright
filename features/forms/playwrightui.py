
from playwright.sync_api import sync_playwright,Playwright
from features.Config.configmanager import ConfigurationManager



class PlaywrightUI:
    def __init__(self):
        self.page = None
        self.config = ConfigurationManager()
        self.browser_type = self.config.obj_config['execution']['browser']
        self.browser_headless = self.config.obj_config['execution']['headless']
        self.screen_shot=self.config.obj_config['execution']['screen_shot']
        self.current_exec=self.config.obj_config['execution']['current_exec']
        self.current_module = self.config.obj_config['execution']['current_module']
        self.base_url=self.config.obj_config[self.current_exec][self.current_module]['url']
        self.user= self.config.obj_config[self.current_exec][self.current_module]['user']
        self.pwd=self.config.obj_config[self.current_exec][self.current_module]['pwd']


        self.playwright,self.browser = self.create_playwright()
    def create_playwright(self):
        playwright = sync_playwright().start()
        browser = getattr(playwright, self.browser_type).launch(headless=self.browser_headless)
        return playwright, browser



    def navigate_url(self, url):
        try:

            with sync_playwright() as p:
                browser = p[self.browser_type].launch(headless=self.browser_headless, slow_mo=6000)
                self.page = browser.new_page()
                self.page.goto(url)
        except Exception as e:
            print("An error occurred:", str(e))
        finally:

            print("Exiting the try-except block")

    def login(self):
        try:
                self.page = self.browser.new_page()
                self.page.goto(self.base_url)
                self.page.get_by_placeholder("Username").click()
                self.page.get_by_placeholder("Username").fill(self.user)
                self.page.get_by_placeholder("Password").click()
                self.page.get_by_placeholder("Password").fill(self.pwd)
                self.page.get_by_role("button", name="Login").click()




        except Exception as e:
            print("An error occurred:", str(e))



    def validate_page_title(self, pstr_title):
        try:

            assert self.page.title() == pstr_title

        except Exception as e:
            print("An error occurred:", str(e))


    def launch_mobile_device(self):
        try:
            with sync_playwright() as p:
                iphone_13 = p.devices['iPhone 13']
                browser = p.webkit.launch(headless=self.browser_headless)
                context = browser.new_context(
                    **iphone_13,
                )
                page = context.new_page()

                # Navigate to a website
                page.goto('https://example.com')

        except Exception as e:
            print("An error occurred:", str(e))
        finally:

            print("Exiting the try-except block")

    def validate_dashboard_page(self):
        try:
            dashboard_element = self.page.locator("xpath=//a[text()='Dashboard']")
            dashboard_text = dashboard_element.text_content()
            assert dashboard_text=="Dashboard"




        except Exception as e:
            print("An error occurred:", str(e))
        finally:

            print("Exiting the try-except block")