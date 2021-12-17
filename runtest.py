import HTMLTestRunner
import unittest

from config.globalparameter import report_name, test_case_path

suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')

# 执行测试
if __name__ == "__main__":
    report = report_name + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'登录页面自动化测试',
        description=u'网络正常'
    )
    runner.run(suite)
