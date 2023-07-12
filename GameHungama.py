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
# open Games Functionality
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Games']").click()
time.sleep(2)
# opening first game Puzzle
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout"
                    "/android.widget.ScrollView/android.widget.RelativeLayout[2]/androidx.viewpager.widget.ViewPager"
                    "/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]"
                    "/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout/android.view.ViewGroup/"
                    "android.widget.ImageView").click()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout"
                    "/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout"
                    "/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat").click()
time.sleep(10)
driver.save_screenshot('Screenshot/games.png')
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                    "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                    "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.TextView").click()
time.sleep(1)
driver.back()
# opening Second game scroll until next game
scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Two Players").instance(0))')
action = TouchAction(driver)
action.long_press(scroll).perform()
time.sleep(2)
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                    "/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView"
                    "/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout"
                    "/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[2]/androidx.recyclerview.widget.RecyclerView"
                    "/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout"
                    "/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout"
                    "/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat").click()
time.sleep(5)

driver.save_screenshot('Screenshot/games2.png')
driver.back()
driver.find_element(By.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                    "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout"
                    "/android.widget.LinearLayout/android.widget.LinearLayout/androidx.appcompat.widget.LinearLayoutCompat[1]").click()
time.sleep(1)
driver.back()
driver.save_screenshot('Screenshot/games_home.png')

driver.quit()