import time

import keyboard
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

caps = {}
caps["appium:deviceName"] = "Android"
caps["platformName"] = "Android"
caps["appium:appPackage"] = "com.hungama.myplay.activity"
caps["appium:appActivity"] = "com.hungama.music.ui.main.view.activity.MainActivity"
caps["appium:noReset"] = "true"
caps["appium:uiautomator2ServerInstallTimeout"] = "200000"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
time.sleep(10)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/ivTabMusicAnim").click()
scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Popular Albums").instance(0))')
action = TouchAction(driver)
action.long_press(scroll).perform()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/ivUserImage").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llPlayAllArtist").click()

time.sleep(10)

driver.quit()