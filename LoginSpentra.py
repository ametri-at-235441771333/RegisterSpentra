import time

from appium import webdriver
from selenium.webdriver.common.by import By

caps = {}
caps["appium:deviceName"] = "Android"
caps["platformName"] = "Android"
caps["appium:noReset"] = True
caps["appium:uiautomator2ServerInstallTimeout"] = 200000
caps["appium:app"] = "C:\\Users\\sudha\\Downloads\\app-1260-14Jun2023.apk"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
time.sleep(2)
driver.find_element(By.ID, "com.spentra:id/tv_skip").click()
time.sleep(2)
driver.find_element(By.ID, "com.spentra:id/loginBtn").click()
time.sleep(1)

# username and password
driver.find_element(By.ID, "com.spentra:id/usernameEdit").send_keys("Akshay")
driver.find_element(By.ID, "com.spentra:id/passwordEdit").send_keys("123456")
driver.find_element(By.ID, "com.spentra:id/loginBtn").click()

time.sleep(15)
driver.quit()
