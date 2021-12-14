# coding:utf-8

from src.common import Base_page
from appium.webdriver.common import mobileby


class Login_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 账号输入框
    user = (by.ID, "com.tencent.mm:id/bxz")
    # 密码输入框
    password = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
    # 登录按钮
    enter_button = (by.ID, "com.tencent.mm:id/hi4")
    # 注册按钮
    register_button = (by.ID, "com.tencent.mm:id/hil")
    # “下一步”按钮
    nextstep_button = (by.ID, "com.tencent.mm:id/fz0")
    # 提示框“我知道了”按钮
    allow_button = (by.ID, "com.tencent.mm:id/ffp")
    # 提示框“允许”按钮
    allow_button1 = (by.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 登录失败弹框
    login_failure = (by.ID, "com.tencent.mm:id/ffh")

    # 输入手机号码
    def input_user(self, username):
        self.send_keys(username, *self.user)

    # 输入密码
    def input_password(self, pwd):
        self.send_keys(pwd, *self.password)

    # 点击登录按钮
    def click_enter_button(self):
        self.find_element(*self.enter_button).click()

    # 点击注册按钮
    def click_register_button(self):
        self.find_element(*self.register_button).click()

    # “下一步”按钮
    def click_nextstep_button(self):
        self.find_element(*self.nextstep_button).click()

    # 提示框“我知道了”按钮
    def click_allow_button(self):
        self.find_element(*self.allow_button).click()

    # 权限弹框“允许”按钮
    def click_allow_button1(self):
        self.find_element(*self.allow_button1).click()

    # 登录失败弹框
    def login_failure(self):
        self.find_element(*self.login_failure)