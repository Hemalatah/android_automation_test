### Demo Application Description

I used an application with basic UI interactions. In this application, I automated four features and wrote 8 test cases. Below are the screen shots of some of the tested pages in the application.

<img src="https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Home%20Page.png" width="10%">
![Home Page]("https://github.com/Hemalatah/android_automation_test/blob/master/Screen_shots/Home%20Page.png"){:height="24px" width="48px"}
![WiFi Settings Test]()
![Log Press Test]()
![Drag And Drop Test]()
![Slider test]()

### Description about the Automation

I used Appium framework for automating the tests in the above pages. Scripts are written in Python using Unittest Module and other supported libraries. Used Android Studio to get the emulator through ADB server to test teh automation. For writing the automation scripts using python, UI element attributes are identified by UIAutomatorViewer.

Below is the workflow in Appium Automation:

Test Script --------> Appium Server ---------------> Android device(Emulator)
       (Appium APIs)       (ADB and Appium uiautomator APIs)
    
