### Demo Application Description

I used an application with basic UI interacting elements like checkbox, slider, press-and-hold, Drag-and-drop and Text Field. In this application, I automated four features and wrote 8 test cases. I also wrote the manual test cases in the EXCEL Sheet attached in this repositry as *Appium_Demo UI Test Cases.xlsx*.

A simple demo of one the features I automated.

![](https://github.com/Hemalatah/android_automation_test/blob/master/Demo/demo.gif)

Below is the home page of the application.

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Home%20Page.png" width="30%">

Demo videos are included in *Demo* folder that has the videos of each test case automation.
Note: 1. Every demo videos are named after its python test case method
      2. Also check the manual test cases in *Appium_Demo UI Test Cases.xlsx* where the python test case method is mentioed for all the test cases.

### Description about the Automation

I used Appium framework for automating the tests in the above pages. Scripts are written in Python using Unittest Module and other supported libraries. Used Android Studio to get the emulator through ADB server to test teh automation. For writing the automation scripts using python, UI element attributes are identified by UIAutomatorViewer.

Below is the workflow in Appium Automation:
<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Appium%20Workflow.png" width="70%">

### High Level picture of Test Cases(Videos attached for all the test cases)

##### Test Case for WiFi Settings:
For checking whether the user is allowed to enter the text in the text field after the field is enabled with the checkbox, I used the below page:

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/WiFi_Settings_tests.png" width="30%">

##### Test Case for Clock Functinality:
This test case is to check whether the clock responds properly when the user change the value of hours and minutes. If the clock ticker is moved to the user expected value, then the test is valid!

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Slider_test.png" width="30%">

##### Test Case for Make Hidden Visible:
This test checks whether the hidden object is visible when the user do some actions. In this scenario, the preferred action is drag and drop.

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Drag_And_Drop_test.png" width="30%">

##### Test Case for Long Press:
When the user tap-and-holds a tab, the tab should be respondede with a popup window. But the actual tab also do lists some sub-lists when it is just pressed and released.

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Long_Press_test.png" width="30%">

