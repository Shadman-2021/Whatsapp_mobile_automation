import unittest
from appium import webdriver
import time


class SendText(unittest.TestCase):
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

    def test_search_number_send_text(self):
        search_button = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Search"]')
        search_button.click()

        search_box = self.driver.find_element_by_id("com.whatsapp:id/search_input")
        search_box.send_keys("01680041124")

        msg = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout')
        msg.click()

        text_input = self.driver.find_element_by_id('com.whatsapp:id/entry')
        text_input.send_keys("Hell!!")

        send_button = self.driver.find_element_by_id("com.whatsapp:id/send")
        send_button.click()

        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SendText)

    unittest.TextTestRunner(verbosity=1).run(suite)
    print('Complete')
