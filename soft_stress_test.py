#coding: utf-8

import os
import re
import multiprocessing
import uiautomator2 as u2

RK_TOTAL = 10
RK_NUMBER_RULE_BEGIN_CHANGE = 7

# d = u2.connect('9786d22636ce6112')
def getRKId():
    rk_id_dict = {}
    f = os.popen('adb devices -l')
    lines = f.readlines()
    for i in range(RK_TOTAL):
        for line in lines:
            if i < RK_NUMBER_RULE_BEGIN_CHANGE-1:
                is_search_result = re.search("device usb:1-1."+str(i+1),line)
            else:
                is_search_result = re.search("device usb:1-1.7."+str(i-5),line)
            if is_search_result:
                rk_id_dict[i+1]=line.split(' ')[0]
                print(rk_id_dict[i+1])
    return rk_id_dict

def performAntutu(rk_id):
    d = u2.connect(rk_id)
    d.press('home')
    d.app_start('com.antutu.ABenchMark')
    d(text="压力测试").click()
    for i in range(2):
        print(i)
        if d(text='立即测试').exists:
            d(text="立即测试").click()
        if d(text='重新测试').exists:
            d(text="重新测试").click()
        while d(text='停止测试').exists:
            pass

if __name__ == '__main__':

    rk_id_dict = getRKId()

    if not rk_id_dict:
        for i in range(RK_TOTAL):
            print("/////////////////////////")
            print(rk_id_dict.get(i+1))
            # perform_make_sd = multiprocessing.Process(target=performAntutu, args=(rk_id_dict.get(i+1)))
            # perform_make_sd.start()



















    # while True:
    #     if d(text="停止测试").wait(timeout=3.0):
    #         continue
    #     else:
    #         break
        # d = u2.connect('2da1b45467f9028d')
        # d.watcher("DECLINE").when(description="允许").click()
        # d(resourceId ="com.antutu.ABenchMark:id/title", text =u"允许").click()

        # d(text='立即测试').exists







# sess = d.session('com.antutu.ABenchMark')
# print(d.info)


# import uiautomator2

# d = uiautomator2.Device('9786d22636ce6112', adb_server_host='192.168.31.234', adb_server_port=5037)


# DATA_PATH = 'D:\Git_project\zynq_mk_sd\ceshi.txt'

# sd_name = ['sdc', 'sdd', 'sda']

# print(sd_name)
# i = 0
# with open(DATA_PATH,'r') as f:
#     print (len(sd_name))
#     lines = f.readlines() # 读取所有行
#     for line in lines:
#         for i in range(len(sd_name)):
#             # print("i:%d" % i)
#             # print(sd_name[i])
#             if line.startswith('/dev/'+ sd_name[i]):
#                 mount_point = line.split(' ')[-1]
#                 cmd = 'umount ' + mount_point
#                 print(cmd)
#             else:
#                 pass
#                 # print("no i :%d" % i)
#                 # break
#             # i = i + 1
#             # print(i)

