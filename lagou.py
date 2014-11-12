# -*- coding: utf-8 -*-
import urllib2,re
import MySQLHelper
#url=u'http://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?kd=%E6%B5%8B%E8%AF%95&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city=%E5%8C%97%E4%BA%AC&requestId=&pn=1'
class Lagou:
    def lagouurls(self,searchurl):
        url=searchurl
        lagouhtml=urllib2.urlopen(url)
        slagouhtml=lagouhtml.read()
        #a=u"jobs/(.*).html"
        title="jobs/(.*)\.html\?source=search\" title=\"(.*)\" target=\"_blank\""
        #b=re.compile(a)
        retitle=re.compile(title)
        urllist=retitle.findall(slagouhtml)
        #print urllist
        return urllist
        '''
        for y in urllist:
            print y[0]
            list1=[int(y[0]),y[1],'http://www.lagou.com/jobs/'+y[0]+'.html?source=search']
            print list1
            dict1={'urladdr_code':list1[0],'urladdr_title':list1[1],'urladdr_url':list1[2]}
            print dict1
            return dict1
        '''
        #print b.findall(c)
        #print urllist
if __name__ == '__main__':
    mysqltest=MySQLHelper.MySQLHelper('127.0.0.1','root','root',3306)
    mysqltest.selectDb('lagou')
    searchurl='http://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?kd=%E6%B5%8B%E8%AF%95&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city=%E5%8C%97%E4%BA%AC&requestId=&pn='
    lagou=Lagou()
    for x in xrange(1,31):
        urllist=lagou.lagouurls(searchurl+str(x))    
        for y in urllist:
            #print y[0]
            list1=[int(y[0]),y[1],'http://www.lagou.com/jobs/'+y[0]+'.html?source=search']
            #print list1
            dict1={'urladdr_code':list1[0],'urladdr_title':list1[1],'urladdr_url':list1[2]}
            print dict1
            mysqltest.insert('urladdr',dict1)