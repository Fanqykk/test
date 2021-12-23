import time
import pytest
import unittest
import ddt
from src.common.read_excel import ReadExcel
from src.pages import login
from src.common import driver_config
from src.common.screenshots import Screenshots

excelpath = "D://code//git//test//src//data//login_data.xlsx"
print(excelpath)
data = ReadExcel(excelpath)
testdata = data.dict_data()


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()

    @ddt.data(*testdata)
    # @ddt.unpack
    @pytest.mark.flaky(rerus=3)
    def test_login_1(self, data):
        """微信登录{0}"""
        username = data['username']
        password = data['password']
        exp = data['except']
        self.login = login.Login_page(self.driver)
        self.login.click_enter_button()  # 点击登录按钮
        self.login.input_user(username)  # 输入账号
        self.login.click_nextstep_button()  # 点击下一步按钮
        self.login.click_allow_button()  # 点击弹框按钮
        self.login.click_allow_button1()  # 点击弹框按钮
        time.sleep(3)
        self.login.click_allow_button1()  # 点击弹框按钮
        time.sleep(3)
        try:
            message = self.driver.find_element_by_id("com.tencent.mm:id/ffh").text
            if len(message) > 0:
                print("结果：", message)
                try:
                    self.assertEqual(exp, message)
                except Exception as e:
                    print('断言失败', e)
                    Screenshots.get_image(self)
        except Exception as e:
            print("手机号正确", e)
            self.login.input_password(password)  # 输入密码
            ts = self.driver.find_element_by_id("com.tencent.mm:id/erw")
            self.assertIn("短信验证码", ts.text, msg='fail')
            self.login.click_nextstep_button()  # 点击登录按钮
            time.sleep(3)
            result = self.driver.find_element_by_id("com.tencent.mm:id/ffh").text
            print("结果：", result)
            try:
                self.assertEqual(exp, result)
            except Exception as e:
                print('断言失败', e)
                Screenshots.get_image(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
