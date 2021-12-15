# !/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import time
import os

devices_list_finally = []
file_list_finally = []
choose_file_num = []


# 检查是否有设备连接PC
def check_devices_link():
    devices_list_start = []
    devices_cmd = os.popen('adb devices').readlines()
    devices_list_start_count = len(devices_cmd)
    devices_list_start_count = devices_list_start_count - 2
    if devices_list_start_count >= 1:
        print('\nfind devices linked')
        for devices_num in range(devices_list_start_count):
            devices_list_start.append(devices_cmd[devices_num + 1])
            device_list_pers = devices_list_start[devices_num].index('\t')
            devices_list_finally.append(devices_list_start[devices_num][:device_list_pers])
            print('devices list :' + '%d  ' % (devices_num + 1) + '%s' % devices_list_finally[devices_num])
            # print(type(devices_list_finally))
        check_local_file()
    else:
        print('Can not find devices link...please check device link...')


# 检查本地文件是否存在
def check_local_file():
    file_list = glob.glob('*.apk')
    file_index = len(file_list)
    if file_index != 0:
        if file_index == 1:
            print('\none local file')
            file_list_finally.append(file_list[0])
            install_apk()
        elif file_index > 1:
            print('\nmore than one local files')
            print('please chose one apk that you want to install:')
            for file_num in range(file_index):
                file_list_finally.append(file_list[file_num])
                choose_file_num = file_num
                install_apk(choose_file_num)
    else:
        print('Can not find local file. please check local file...')

# 安装应用
def install_apk(choose_file_num= 0):
    file_path = os.getcwd()
    for install_apk_to_devices_index in range(len(devices_list_finally)):
        print('adb -s' + ' '+ devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' '+file_path + '\\' +file_list_finally[choose_file_num])
        os.system('adb -s' + ' '+ devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' '+file_path+ '\\' + file_list_finally[choose_file_num])
    time.sleep(3)
    print('      *       *       *  ')
    print('    *    *    *     *   ')
    print('   *      *   *   *   ')
    print('   *      *   *  *     ')
    print('   *      *   *    *   ')
    print('    *   *     *      *')
    print('      *       *        * ')


check_devices_link()