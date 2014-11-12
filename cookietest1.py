import cookielib,urllib2,os,urllib

#ckjar = cookielib.MozillaCookieJar(os.path.join('C:', 'cookies.txt'))
ckjar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar) )
urllib2.install_opener(opener)
data={'accountName':'admin','passWord':'1'}
post_data=urllib.urlencode(data)
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
req = urllib2.Request('http://202.97.194.220:7023/openbid/platform/permission/kbLoginAction.action',post_data,headers)
resp = urllib2.urlopen(req)
respInfo = resp.info()
print respInfo

f = opener.open(req) 
htm = f.read()
print htm

'''req1=urllib2.Request('http://202.97.194.220:7023/openbid/kb/kbAbandonAction!abandonTendererList.action')
f = opener.open(req1) 
htm1 = f.read()
print htm1
#f.close()
'''