# 引入模块
import glob
import time
import os

# 定义全局变量
devices_list_finally = []
file_list_finally = []
chose_file_num = []

# 检查本地文件是否存在
def check_local_file():
    file_list = glob.glob('*.apk')
    # print (file_list)
    file_index = len(file_list)
    if file_index != 0:
        # print('%s, %d' %(file_list, file_index))
        if file_index == 1:
            print('one local file')
            install_apk()
        elif file_index > 1:
            print('more than one local files')
            print('PLEASE chose one apk that you want to install')
            for file_num in range(file_index):
                file_list_finally.append(file_list[file_num])
                print('%d: %s ' % (file_num + 1, file_list[file_num]))
            chose_file = input('Enter num to chose apk:>>')
            # print(type(chose_file))
            try:
                chose_file_num  = int(chose_file)
                if type(chose_file_num) is int:
                    chose_file_num = chose_file_num - 1
                    print('will go to install apk')
                    install_apk(chose_file_num)
                else:
                    print('your enter is err,please check it...')
                    check_local_file()
            except ValueError:
                print('you enter vslue is err,please check it.. ')
                time.sleep(3)
                check_local_file()


    else:
        print('Can not find local file. plase check local file...')

# 安装应用
def install_apk(chose_file_num= 0):
    file_path = os.getcwd()
    for install_apk_to_devices_index in range(len(devices_list_finally)):
        # print('adb -s' + ' '+ devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' '+file_path + '\\' +file_list_finally[chose_file_num])
        os.system('adb -s' + ' '+ devices_list_finally[install_apk_to_devices_index] + ' ' + 'install' + ' '+file_path+ '\\' + file_list_finally[chose_file_num])

    print('      *       *       *  ')
    print('    *    *    *     *   ')
    print('   *      *   *   *   ')
    print('   *      *   *  *     ')
    print('   *      *   *    *   ')
    print('    *   *     *      *')
    print('      *       *        * ')

# 检查是否有设备连接PC
def check_devices_link():
    devices_list_start = []

    devices_cmd = os.popen('adb devices').readlines()
    devices_list_start_count = len(devices_cmd)
    devices_list_start_count = devices_list_start_count - 2
    if devices_list_start_count >= 1:
        print('find devices linked')
        for devices_num in range(devices_list_start_count):
            devices_list_start.append(devices_cmd[devices_num + 1])
            # print(devices_list_start)
            device_list_pers = devices_list_start[devices_num].index('\t')
            # print(device_list_pers)
            devices_list_finally.append(devices_list_start[devices_num][:device_list_pers])
            print('devices list :' + '%d  '%(devices_num+1)+ '%s'% devices_list_finally[devices_num])
            # print(type(devices_list_finally))
        check_local_file()
    else:
        print('Can not find devices link...pls check device link...')

# ====================start====================

    check_devices_link()
