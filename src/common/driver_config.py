from appium import webdriver


class Driver_Config():
    def get_driver(self):
        try:
            desired_caps = {'platformName': 'Android',  # 平台名称
                            'platformVersion': '7.1.2',  # 系统版本号
                            'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                            'appPackage': 'com.tencent.mm',  # apk的包名
                            'appActivity': 'com.tencent.mm.ui.LauncherUI',  # activity 名称
                            'ensureWebviewsHavePages': True
                            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 连接Appium
            self.driver.implicitly_wait(8)

            return self.driver
        except Exception as e:
            raise e
