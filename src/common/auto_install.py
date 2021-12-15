# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


class appInstall:
    def __init__(self, path):
        self.path = path

    def auto_install(self):
        # 获取path路径下的所有文件
        files = os.listdir(self.path)
        for file in files:
            if file[len(file) - 3:len(file)] == "apk":
                string = 'adb install %s\\\\"%s\"' % (self.path, file)
                print(string)
                os.popen(string)
                print(" 正在安装中....")
                time.sleep(5)
                print("安装完成")
        else:
            time.sleep(60)
            print("finished")
            time.sleep(1000)


if __name__ == '__main__':
    path = input("请输入apk所在文件路径:")
    app = appInstall(path)
    app.auto_install()

