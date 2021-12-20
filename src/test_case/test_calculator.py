import os
import time
import unittest
from appium import webdriver


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.youdao.calculator',  # apk的包名
                        'appActivity': 'com.youdao.calculator.activities.MainActivity',  # activity 名称
                        'ensureWebviewsHavePages': True
                        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """计算器测试"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x0 = window['width'] * 0.8  # 起始x坐标
        x1 = window['width'] * 0.2  # 终止x坐标
        y = window['height'] * 0.5  # y坐标
        for i in range(n):
            self.driver.swipe(x0, y, x1, y, t)
            time.sleep(1)
        self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()
        for i in range(5):
            self.driver.find_element_by_id('com.youdao.calculator:id/view_empty_container').click()
            time.sleep(1)

        self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[17]/android.widget.FrameLayout").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[20]/android.widget.FrameLayout/android.widget.ImageView").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[9]/android.widget.FrameLayout").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[25]/android.widget.FrameLayout").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageButton[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.youdao.calculator:id/actionbar_history_view").click()
        time.sleep(2)
        error_mes = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView").text
        try:
            assert error_mes == u'aaaa历史记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            # 截图路保存径，绝对路径，也可以用相对路径
            screenshoturl = r"D:\code\git\test\src\report\images\\"
            # 时间样式
            timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
            # 寻找失败时自动截图至指定目录images，截图名称为 时间戳 + png后缀
            imgPath = os.path.join(screenshoturl, '%s.png' % str(timestrmap))
            self.driver.save_screenshot(imgPath)
            print('screenshot:', timestrmap, '.png')

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()
