#standard python packges
import os
import unittest

#Appium python package
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains

def func():
    raise Exception("Error Occured!")

 
class AppiumDemoTests(unittest.TestCase):
    """ Class that implements the  test cases for AppiumDemo App
    """

    def test_error(self):
        with self.assertRaises(Exception): func()

    def setUp(self):
        """ Function that establishes the connection with Appium server
        and loads the Application to emulator via Appium server. Appium server
        used Android UIAutomator/adb_server to enable the automated testing
        """
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Pixel (Edited)'
        desired_caps['newCommandTimeout'] = '60000'
        desired_caps['automationName'] ='uiautomator2'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'ApiDemos-debug.apk'))
        desired_caps['appPackage'] = "io.appium.android.apis"
        desired_caps['appActivity'] = "ApiDemos"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(50)

        
    # def test_Slide(self):
        
    #     #self.driver.implicitly_wait(10)

    #     "Click on Views"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']").click()

    #     "Select the Date Widgets"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Date Widgets']").click()

    #     "Select Inline element using UIAutomator"
    #     self.driver.find_element_by_android_uiautomator("text(\"2. Inline\")").click()

    #     "Select the time 2:30"
    #     self.driver.find_element_by_xpath("//*[@content-desc='2']").click()

    #     "Call the touch method"
    #     touch = TouchAction(self.driver)

    #     "Select the time 2:10"
    #     first = self.driver.find_element_by_xpath("//*[@content-desc='10']").click()

    #     "Select the time 2:50"
    #     second = self.driver.find_element_by_xpath("//*[@content-desc='50']").click()

    #     "Call the long press method to move the minutes"
    #     touch.long_press(first).move_to(second).release().perform()

    # def test_Long_press(self):
        
    #     #self.driver.implicitly_wait(10)

    #     "Click on Views"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']").click()
        
    #     "Call the touch method from unittest module"
    #     touch = TouchAction(self.driver)
    #     el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Expandable Lists']")
        
    #     "Perform tap operation"
    #     touch.tap(el).perform()
        
    #     "Click on 1. Custom Adapter"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='1. Custom Adapter']").click()
        
    #     "Select Fish Names"
    #     fish = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Fish Names']")
        
    #     "Long press on it to check whether the content is displayed "
    #     touch.long_press(fish).release().perform()
       
    #     "Check whether the selected element has displayed all the sub-elements"
    #     el = self.driver.find_element_by_id("android:id/title")
    #     print(el)
    #     self.assertEqual(True, (self.driver.find_element_by_id("android:id/title").is_displayed()))

    # def test_Drag_and_drop(self):

    #     #self.driver.implicitly_wait(10)

    #     "Click on Views"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']").click()

    #     "Click on drag and drop"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Drag and Drop']").click()

    #     "Select the draggable element"
    #     source = self.driver.find_elements_by_class_name("android.view.View")[0]

    #     "Select the droppable element"
    #     dest = self.driver.find_elements_by_class_name("android.view.View")[1]

    #     "Call the touch method"
    #     touch = TouchAction(self.driver)

    #     "Call the long press method to drag and drop"
    #     touch.long_press(source).move_to(dest).release().perform()

    # def test_Scroll(self):

    #     #self.driver.implicitly_wait(10)

    #     "Click on Views"
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Views']").click()

    #     "Initiate scrolling"
    #     self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"WebView\"))")

    

    def checkbox_enabled(self):
        """ checks if the checkbox is enabled 
            return True if enabled else False
        """
        return self.driver.find_element_by_id("android:id/checkbox").get_attribute("checked")

    def checkbox_toggle(self):
        """ Toggles the checkbox
        """
        self.driver.find_element_by_id("android:id/checkbox").click()

    def init_wifi_settings(self):
        """ Navigate from Home page to Wifi settings
        """

        "Click on Preferences from the list"
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']").click()

        "Select the 3. Preference dependencies"
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']").click()

        if self.checkbox_enabled():
            self.checkbox_toggle()

        return


    def test_WiFi_Checkbox_Validation(self):

        """Navigate to the test page and initialize the checkbox"""
        self.init_wifi_settings()

        "Click on Checkbox preference"
        self.checkbox_toggle()

        
        "To find whether the checkbox element is selected or not"
        isChecked = self.driver.find_element_by_id("android:id/checkbox").get_attribute("checked")
        if(not isChecked):
            assert(0)



    def test_WiFi_Settings_Enable_Validation(self):

        """Navigate to the test page and initialize the checkbox"""
        self.init_wifi_settings()

        "Click on Checkbox preference"
        self.checkbox_toggle()

        "To find whether the WiFi setting tab is active"
        isEnabled = self.driver.find_elements_by_class_name("android.widget.LinearLayout")[2].get_attribute("enabled")
        if(not isEnabled):
            assert(0)

    def test_WiFi_Settings_Disable_Validation(self):

        """Navigate to the test page and initialize the checkbox"""
        self.init_wifi_settings()

        "To find whether the WiFi setting tab is active"
        isEnabled = self.driver.find_elements_by_class_name("android.widget.LinearLayout")[2].get_attribute("enabled")
        
        if(isEnabled):
            assert(0)

    def test_WiFi_Settings_Text_Field_Validation(self):

        set_name = "Appium_Demo"

        "Click on Preferences from the list"
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']").click()

        "Select the 3. Preference dependencies"
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']").click()

        "Click on Checkbox preference"
        self.driver.find_element_by_id("android:id/checkbox").click()

        "Select the second element in the grid using indexing"
        self.driver.find_element_by_xpath("(//android.widget.RelativeLayout)[2]").click()

        "Enter text in the text field"
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(set_name)

        "Click the ok button"
        self.driver.find_elements_by_class_name("android.widget.Button")[1].click()

        """Check whether the text is saved when the current page is on"""

        "Select the WiFi setting tab again"
        self.driver.find_element_by_xpath("(//android.widget.RelativeLayout)[2]").click()

        "Get the text from the text field and check"
        get_name = self.driver.find_element_by_class_name("android.widget.EditText").text
        if(set_name != get_name):
            print("set name: {}, get name: {}".format(set_name, get_name))
            assert(0)


    def tearDown(self):

        "Tear down the test"
        self.driver.quit()


### Main Script
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumDemoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


    
