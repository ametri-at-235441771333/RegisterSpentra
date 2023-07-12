import time

from appium import webdriver
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
driver.find_element(By.ID, "com.hungama.myplay.activity:id/ivUserPersonalImage").click()
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llLoginWithMobile").click()
time.sleep(2)
MoNUmber=driver.find_element(By.ID, "com.hungama.myplay.activity:id/etMobileNumber")
MoNUmber.send_keys("9686171272")
time.sleep(4)
driver.find_element(By.ID,"com.hungama.myplay.activity:id/btnSendOTP").click()
time.sleep(15)
driver.find_element(By.ID,"com.google.android.gms:id/positive_button").click()
time.sleep(5)

driver.quit()