import time
import os


class Screenshots():
    def get_image(self):
        try:
            # 截图路保存径，绝对路径，也可以用相对路径
            screenshoturl = r"C:\ProgramData\Jenkins\.jenkins\workspace\python_autotest\src\report\images\\"
            # screenshoturl = r"D:\code\git\test\src\report\images\\"
            # 时间样式
            timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
            # 寻找失败时自动截图至指定目录images，截图名称为 时间戳 + png后缀
            imgPath = os.path.join(screenshoturl, '%s.png' % str(timestrmap))
            self.driver.save_screenshot(imgPath)
            print('screenshot:', timestrmap, '.png')
        except Exception as e:
            raise e
