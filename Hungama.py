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
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llLibrary").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/tvTitle").click()
time.sleep(2)
createPlaylist=driver.find_element(By.ID, "com.hungama.myplay.activity:id/etCreatePlaylist")
createPlaylist.clear()
createPlaylist.send_keys("MyList")
time.sleep(2)
driver.find_element(By.ID,"com.hungama.myplay.activity:id/vBtnCreate").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llAddSongs").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/ivAddSong").click()
time.sleep(5)
driver.quit()