# -*- coding: utf-8 -*-
import urllib2,re
import MySQLHelper

#print listurl
#print listurl[0]['urladdr_url']
class LagouInfo:
    def gethtmlforre(self,jobstr,sjobhtml,flags=0):
        self.jobstr=re.compile(jobstr,flags)    
        self.sjobhtml=self.jobstr.findall(sjobhtml)
        return self.sjobhtml[0]
    def getlagouinfo(self,code,url):
        self.url=url
        self.code=code   
        jobhtml=urllib2.urlopen(self.url)
        sjobhtml=jobhtml.read()
        jobtitle="<h1 title=\"(.*)\""
        #salary
        jobsalary="<dd class=\"job_request\">\s*<span class=\"red\">(.*)</span>"
        #area
        jobarea="<span class=\"red\">.*</span>\s*<span>(.*)</span>"
        #经验
        jobexperience="<span>经验(.*)</span>"
        #学历
        jobeducation="<span>经验.*</span>\s*<span> (.*)</span>"
        #职业情况
        jobnatureofwork="<span>经验.*</span>\s*<span>.*</span>\s*<span>(.*)</span>"
        #职位诱惑
        jobseduction="职位诱惑 : (.*)\s*<div>发布时间"
        #b=re.compile(a)
        #title
        jobdescription="<dd class=\"job_bt\">(.*)</dd>.*<dd class=\"unresume\">"
        jobcompanyname="<h2 class=\"fl\">\s*(.*)\s*<img"
        jobfield="<span>领域</span> (.*)</li>"
        jobscale="<span>规模</span> (.*)</li>"
        jobcompanyurl="<span>主页</span>\s*<a href=\"(.*)\" target=\"_blank\""
        jobstageofdevelopment="<span>目前阶段</span> (.*)</li>"
        jobcompanyaddr="<h4>工作地址</h4>\s*<div>(.*)</div>"
        jobcompanyname=self.gethtmlforre(jobcompanyname, sjobhtml)
        jobarea=self.gethtmlforre(jobarea, sjobhtml)
        jobtitle=self.gethtmlforre(jobtitle, sjobhtml)
        jobsalary=self.gethtmlforre(jobsalary, sjobhtml)
        jobseduction=self.gethtmlforre(jobseduction, sjobhtml)
        jobexperience=self.gethtmlforre(jobexperience, sjobhtml)
        jobeducation=self.gethtmlforre(jobeducation, sjobhtml)
        jobnatureofwork=self.gethtmlforre(jobnatureofwork, sjobhtml)
        jobdescription=self.gethtmlforre(jobdescription, sjobhtml,16)#匹配所有字符
        jobfield=self.gethtmlforre(jobfield, sjobhtml)
        jobscale=self.gethtmlforre(jobscale, sjobhtml)
        jobcompanyurl=self.gethtmlforre(jobcompanyurl, sjobhtml)
        jobstageofdevelopment=self.gethtmlforre(jobstageofdevelopment, sjobhtml)
        jobcompanyaddr=self.gethtmlforre(jobcompanyaddr, sjobhtml)
        jobinfolist={'jobinfo_code':self.code, 'jobinf_name':jobtitle, 'jobinfo_salary':jobsalary,
        'jobinfo_area':jobarea, 'jobinfo_experience':jobexperience, 'jobinfo_education':jobeducation,
        'jobinfo_natureofwork':jobnatureofwork, 'jobinfo_seduction':jobseduction, 'jobinfo_description':jobdescription,
        'jobinfo_companyname':jobcompanyname, 'jobinfo_field':jobfield, 'jobinfo_scale':jobscale,
        'jobinfo_companyurl':jobcompanyurl, 'jobinfo_stageofdevelopment':jobstageofdevelopment,
        'jobinfo_companyaddr':jobcompanyaddr}
        return jobinfolist
        #mysqltest.insert('jobinfo', jobinfolist)
if __name__ == '__main__':
    mysqltest=MySQLHelper.MySQLHelper('127.0.0.1','root','root',3306)
    mysqltest.selectDb('lagou')
    #sql="select urladdr_url,urladdr_code from urladdr where urladdr_url like '%148790%'"
    sql="select urladdr_url,urladdr_code from urladdr"
    #print sql
    listurl=mysqltest.queryAll(sql)
    #print listurl
    #print listurl[0]['urladdr_code']
    lagouinfo=LagouInfo()
    for x in listurl:
        jobinfolist=lagouinfo.getlagouinfo(x['urladdr_code'],x['urladdr_url'])
        mysqltest.insert('jobinfo', jobinfolist)
    #jobinfolist=lagouinfo.getlagouinfo(listurl[0]['urladdr_code'],listurl[0]['urladdr_url'])
    #mysqltest.insert('jobinfo', jobinfolist)