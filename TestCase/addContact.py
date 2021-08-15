mport unittest
from appium import webdriver
import time


class AddContact(unittest.TestCase):
    def setUp(self):
        desired_caps = {"platformName": "Android",
                        "appPackage": "com.whatsapp",
                        "appActivity": "com.whatsapp.HomeActivity",
                        "app": "D:\\whatsapp\\WhatsApp.apk",
                        "automationName": "UiAutomator2",
                        "appWaitActivity": "com.whatsapp.HomeActivity",
                        "appWaitDuration": "30000",
                        "fullReset": "False",
                        "deviceName": "emulator-5554",
                        "noReset": "True"}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
