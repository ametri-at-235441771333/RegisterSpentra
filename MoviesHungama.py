import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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
# movies functionality
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Movies']").click()
time.sleep(2)

# Opening first movie
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                              "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout"
                              "/android.widget.ScrollView/android.widget.RelativeLayout[2]/androidx.viewpager.widget.ViewPager"
                              "/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]"
                              "/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat"
                              "/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageView").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llWatchlist").click()
driver.save_screenshot('Screenshot/movies.png')
driver.back()
time.sleep(5)
scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Popular Right Now").instance(0))')
action = TouchAction(driver)
action.long_press(scroll).perform()

#opening second movie

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                              "/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView"
                              "/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout"
                              "/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[3]/androidx.recyclerview.widget.RecyclerView"
                              "/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.RelativeLayout"
                              "/android.view.ViewGroup/android.widget.ImageView").click()
time.sleep(2)
driver.find_element(By.ID, "com.hungama.myplay.activity:id/llWatchlist").click()
driver.save_screenshot('Screenshot/movies2.png')
driver.back()

driver.quit()