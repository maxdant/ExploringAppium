from appium import webdriver
from applitools.selenium import Eyes, Target
from applitools.common.geometry import Region
from APIkeys import api_keys


# Initialize the eyes SDK and set your private API key.
eyes = Eyes()
eyes.api_key = api_keys['eyes']

ignored_region = Region(0, 0, 355, 63)
# Desired capabilities.
desired_caps = dict(
    platformName='Android',
    deviceName='emulator-5554',
    platformVersion='11',
    automationName='UiAutomator2',
    app='https://applitools.bintray.com/Examples/eyes-hello-world.apk')

# Open the app.
wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

try:

    # Start the test.
    eyes.open(driver=wd, app_name='Contacts', test_name='My first Appium native Python test!')

    # Visual UI testing.
    # eyes.check_window('Contact list!')
    eyes.check('Contact list!', Target.window().ignore(ignored_region))

    # End the test.
    eyes.close()

finally:

    # Close the app.
    wd.quit()

    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort_if_not_closed()
