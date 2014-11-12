# -*- coding: utf-8 -*-
#from urllib2 import Request, urlopen, URLError, HTTPError

'''
old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req);
print 'Old url :' + old_url
print 'Real url :' + response.geturl()
print response.info()
'''
import urllib2

# 创建一个密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码

top_level_url = "https://passport.csdn.net/account/login?ref=toolbar"

# 如果知道 realm, 我们可以使用他代替 ``None``.
# password_mgr.add_password(None, top_level_url, username, password)
password_mgr.add_password(None, top_level_url,'auuppp', 'auuppp123')
print password_mgr

# 创建了一个新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# 创建 "opener" (OpenerDirector 实例)
opener = urllib2.build_opener(handler)

a_url = 'http://www.baidu.com/'

# 使用 opener 获取一个URL
opener.open(a_url)

# 安装 opener.
# 现在所有调用 urllib2.urlopen 将用我们的 opener.
urllib2.install_opener(opener)

 

