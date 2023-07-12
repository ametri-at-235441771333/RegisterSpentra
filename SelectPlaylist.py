import time
from appium import webdriver
from selenium.webdriver.common.by import By

caps = {}
caps["appium:deviceName"] = "Android"
caps["platformName"] = "Android"
caps["appium:appPackage"] = "com.hungama.myplay.activity"
caps["appium:appActivity"] = "com.hungama.music.ui.main.view.activity.MainActivity"
caps["appium:noReset"] = True
caps["appium:uiautomator2ServerInstallTimeout"] = 200000
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
time.sleep(10)

driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Charts']").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/ivMore").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llMain").click()
time.sleep(2)
#share story
driver.find_element(By.ID, "com.hungama.myplay.activity:id/threeDotMenu2").click()
time.sleep(1)
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                           "android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.RelativeLayout").click()
driver.save_screenshot('shareStory.png')
time.sleep(1)
driver.back()
time.sleep(2)
#share with friends
driver.find_element(By.ID, "com.hungama.myplay.activity:id/threeDotMenu2").click()
time.sleep(2)
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                           "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout").click()
time.sleep(2)
driver.save_screenshot('shareWithFriends.png')
driver.back()
time.sleep(2)
#add to que
driver.find_element(By.ID, "com.hungama.myplay.activity:id/threeDotMenu2").click()
time.sleep(1)
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                           "/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.RelativeLayout").click()
driver.save_screenshot('addtoQue.png')
driver.back()

time.sleep(10)
driver.quit()