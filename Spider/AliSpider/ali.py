import os
import random
import time
import requests
import re
import csv
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

time.sleep(3)

# 商户页面的URL
# https://s.1688.com/company/company_search.htm?keywords=%BE%C6&n=y&spm=a260k.635.1998096057.d1
url = 'https://s.1688.com/company/company_search.htm?keywords=%BE%C6'

# 登录的url
login_url = 'https://login.taobao.com/member/login.jhtml'

# 跳转到登录页面
driver.get(login_url)
driver.maximize_window()

# 睡眠5秒
time.sleep(5)

#利用selenium的find_element方法选择帐号密码然后进行登录
element=WebDriverWait(driver,60).until(lambda driver :driver.find_element_by_xpath("//*[@id='J_Quick2Static']"))
element.click()
driver.find_element_by_name("TPL_username").send_keys('3382315515@qq.com')#***
driver.find_element_by_name("TPL_password").clear()
driver.find_element_by_name("TPL_password").send_keys('zmq2006zz')#***
driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()

#异地登录，需要输入手机验证码
time.sleep(5)

# 跳转到化工商户页面的url
driver.get(url)

# 防爬虫的UserAgent处理
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1;.NET CLR 1.1.4322; .NET CLR2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5(like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
]

#利用Selunium将Cookie保存下来，便于Requests使用
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookiestr = ';'.join(item for item in cookie)
cookies={}
for line in cookiestr.split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value

csvfile = open('data.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow((
    u'企业名称'.encode('gbk'),
    u'主页'.encode('gbk'),
    u'电话'.encode('gbk'),
    u'地址'.encode('gbk'),
))



#进行数据爬取
for page in range(1, 100):
    #选择爬取每个商户主页的URL
    title = driver.find_elements_by_css_selector("a[class=list-item-title-text]")
    #爬取每个商户联系方式页面，并解析提取
    for i in range(len(title)):
        print (i)
        contact_url = title[i].get_attribute("href") + 'page/contactinfo.htm'
        print(contact_url)
        headers = {'User-Agent': user_agents[random.randint(0,len(user_agents)-1)],
                   'Accept': 'text/html;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'GBK,utf-8;q=0.7,*;q=0.3',
                   'Connection': 'close',
                   'Referer': 'http://www.google.com'}
        r = requests.get(contact_url, headers=headers, cookies=cookies)
        with open("response.html","w")as f :
            f.write(r.text)
        soup = BeautifulSoup(r.text, "html.parser")

        phone_html = soup.find(class_='m-mobilephone')
        phone_num_match = re.match(r'\D*(\d+).*', str(phone_html), re.DOTALL)
        if phone_num_match:
            phone_num = int(phone_num_match.group(1).replace(" ", ""))
        else:
            phone_num = 0

        name_str = title[i].get_attribute("text")
        name_html = soup.find(class_='contact-info')
        name_content_match = re.match(r'.*<h4>(.*)</h4>.*', str(name_html), re.DOTALL)
        if name_content_match:
            name_content = name_content_match.group(1).replace(" ", "")
        else:
            name_content = ''

        address_html = soup.find(class_='address')
        address_content_match = re.match(r'.*s">(.*?)</dd>*', str(address_html), re.DOTALL)
        if address_content_match:
            address_content = address_content_match.group(1).replace(" ", "")
        else:
            address_content = ''

        print(address_content, name_content, phone_num)

        data = (
            name_content.encode('gbk', 'ignore'),
            title[i].get_attribute('href'),
            phone_num,
            address_content
        )
        writer.writerow(data)

        # company_data = {
        #     'company_url':contact_url,
        #     'company_name':name_content,
        #     'company_address':address_content,
        #     'company_phonenum':phone_num,
        # }
        # with open('data.html', 'w') as f:
        #     f.write(str(company_data))

        time.sleep(random.uniform(1,3))

    #进行下一页的爬取
    js = 'var q=document.documentElement.scrollTop=30000'
    driver.execute_script(js)
    time.sleep(1)
    page = driver.find_elements_by_css_selector("a[class=page-next]")
    page = page[0]
    page.click()
    time.sleep(2)

csvfile.close()
driver.close()