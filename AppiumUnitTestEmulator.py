import unittest
from appium import webdriver
import time


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['platformName'] = 'Android'
        self.dc['platformVersion'] = '11'
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['appPackage'] = 'com.google.android.apps.maps'
        self.dc['appActivity'] = 'com.google.android.maps.MapsActivity'

        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
