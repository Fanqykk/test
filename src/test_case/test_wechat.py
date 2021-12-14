import time
import unittest
from appium import webdriver


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.tencent.mm',  # apk的包名
                        'appActivity': 'com.tencent.mm.ui.LauncherUI',  # activity 名称
                        'ensureWebviewsHavePages': True
                        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_wechat(self, t=500, n=4):
        """微信登录"""
        self.driver.find_element_by_id("com.tencent.mm:id/hi4").click()
        el2 = self.driver.find_element_by_id("com.tencent.mm:id/bxz")
        el2.click()
        el2.send_keys("17675480202")
        self.driver.find_element_by_id("com.tencent.mm:id/fz0").click()
        self.driver.find_element_by_id("com.tencent.mm:id/ffp").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(3)
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        el6.send_keys("fasdfdf")
        self.driver.find_element_by_id("com.tencent.mm:id/fz0").click()

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()
