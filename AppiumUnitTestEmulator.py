import unittest
from appium import webdriver
import time
from pages.GMaps import *


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['platformName'] = 'Android'
        # self.dc['platformVersion'] = '11'
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['appPackage'] = 'com.google.android.apps.maps'
        self.dc['appActivity'] = 'com.google.android.maps.MapsActivity'

        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        gmaps = GMaps()
        buttons = self.driver.find_elements_by_class_name('android.widget.Button')
        if len(buttons) > 0:
            for button in buttons:
                if button.text == 'SKIP':
                    button.click()
                    break
        search_box = self.driver.find_element_by_class_name(gmaps.search_box_classname)
        search_box.click()
        enter_input_for_search = self.driver.find_element_by_class_name(gmaps.input_for_search_classname)
        time.sleep(2)  # to remove asap
        enter_input_for_search.send_keys("Berlin")
        berlin_xpath = '//*[contains(@text, "Berlin")] '
        first_result_to_tap = self.driver.find_element_by_xpath(berlin_xpath)
        assert first_result_to_tap.text == 'Berlin'
        first_result_to_tap.click()
        time.sleep(5)  # just for watching the phone

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
