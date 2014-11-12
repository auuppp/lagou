#coding=utf-8
import urllib2
import urllib
import cookielib

def login():
    #email = raw_input("请输入用户名:")
    #pwd = raw_input("请输入密码:")
    #data={"loginName":"政府投资建设工程招标中心","pwd1":"1","flage":"login","mothod":"login"}
    cj=cookielib.CookieJar()   #获取cookiejar实例
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    data={'userName':'孙丽丽_采购科','password':'dqjs2009@'}
    post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式
    #自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
    headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    website = "http://202.97.194.227:7011/sys/loginWeeon.do"
    req=urllib2.Request(website,post_data,headers)
    content=opener.open(req)
    #print content.read()    #linux下没有gbk编码，只有utf-8编码
    #print content.read()
    data1={'sso':'true','sessionMd5':u'wu9PWtkEDYn7wPHeFaDl62jxjmULsY0ZvjUR0M2NBDvo%2Bv%2FmLQPVTN9byDGtuWublSxtsA%2Fzm2LWp81e1dnCIstmMc%2B0LUggG0O7Rj8Ol5gJiEFjfiA4rDn%2BS0QoLZl613s%2F8bK5hL0zao5Ifjn4NliZ9yFv2pC1uaAAVzK9JKJIc1rTpttcPDpn02FEYPOvqEV8dQTuH52nfF19DQ3WrRwBq%2BCK3hxMnNR11wByxCu7vbE754N9iXcAUqGVXJ0vsR4QIES%2FjwxCaYyn%2BKi9jLwSU0BrNggOUmysTHqan%2FhoyvQNmBqg8lKUABFKwlbUdSMIZ23oJQdYcdmSt%2BvqVJHx3fhs3dIgZ9xMgszTRbhPu6eZ5QJBfIWOUs3XkuvjD48e8Og5H6j7sozvUSn%2FszQ%2BnFWLWjfvG%2Fl22DfniTTiDhdABtgYN7fuH1rcGTHilMm6NoLx6nmaX7iakPP9rwTqxKr9LZxBdV9lM8FUAXv6BEydj%2Bu1zw8%2BqzXTvMn0v7vMqmU0UaN8JqOiQcNwznUvYRTNzA7SwfsZP%2BS52acKobHuxoVFOf1TSiZqQ4AYr3aqwIjSaoxNXl2c6Oc4JcH7GT%2FkudmnCqGx7saFRTn9U0omakOAGHQ%2BZVf%2FipN0%2Bc8Yco%2FPFZrB%2Bxk%2F5LnZpwqhse7GhUU5%2FVNKJmpDgBjzykSYhGW2AC47QZe9SLEyIm1Gxz0zKndmZhn8EEsT7jiQUcqVo5r0tOVaF9haWtZzchcLtPtUw9N7kisgNSgJuuqqPDJscqL5g97n4gvkEPpXSDyMw9Cps9cmGrEXQyUV81NFDvvsY%2BSElfMPZhUqSAQBamA2b3UHX%2F8xnesSeI8HSrqaqsGQtX8DSf44rXW2ncTpVDP25BUMx31kDsn6BNo8pyT%2F0W%2BLLkawKdDaAA%3D%3D'}
    post_data1=urllib.urlencode(data1) 
    req=urllib2.Request('http://202.97.194.227:7011/ztb/wz/planOfficial/findPageList.do')
    html1=opener.open(req)
    print html1.read()
login()
