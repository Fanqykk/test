import time
import pytest
import unittest
from src.data.data import *
from ddt import data, ddt, unpack
from src.pages import login
from src.common import driver_config


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()

    @data(*get_log_data())
    @unpack
    @pytest.mark.flaky(rerus=3)
    def test_login_1(self, username, password):
        """微信登录"""
        self.login = login.Login_page(self.driver)
        self.login.click_enter_button()  # 点击登录按钮
        self.login.input_user(username)  # 输入账号
        self.login.click_nextstep_button()  # 点击下一步按钮
        self.login.click_allow_button()  # 点击弹框按钮
        self.login.click_allow_button1()  # 点击弹框按钮
        time.sleep(3)
        self.login.click_allow_button1()  # 点击弹框按钮
        time.sleep(3)
        self.login.input_password(password)  # 输入密码
        ts = self.driver.find_element_by_id("com.tencent.mm:id/erw")
        self.assertIn("短信验证码", ts.text, msg='fail')
        self.login.click_nextstep_button()  # 点击登录按钮
        time.sleep(3)
        '''
        error_mes = self.driver.find_element_by_id("com.tencent.mm:id/ffh").text
        print(error_mes)
        try:
            assert error_mes == u'帐号或密码错误，请重新填写。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
        '''

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
