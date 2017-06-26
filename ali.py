import time
import urllib.request
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent

from urllib3.connectionpool import xrange

binary = FirefoxBinary("/usr/lib/firefox")
driver = webdriver.Firefox(firefox_binary=binary)

time.sleep(3)
# 商户页面的URL
# https://s.1688.com/company/company_search.htm?keywords=%BE%C6&n=y&spm=a260k.635.1998096057.d1
url = 'https://s.1688.com/company/company_search.htm?keywords=%BE%C6&button_click=top&earseDirect=false&n=y'
# 登录的url
login_url = 'https://login.taobao.com/member/login.jhtml'
# 跳转到登录页面
driver.get(login_url)
# 睡眠5秒
time.sleep(5)
#利用selenium的find_element方法选择帐号密码然后进行登录
driver.find_element_by_css_selector("@TPL_username_1").send_keys("*******")
driver.find_element_by_css_selector("@TPL_password_1").send_keys('*******码')
driver.find_element_by_css_selector("@J_SubmitStatic").click()
# 睡眠5秒
time.sleep(5)
# 跳转到化工商户页面的url
driver.get(url)
# 防爬虫的UserAgent处理
ua=UserAgent()

for page in xrange(1, 100):
    #寻找查找页面的所有商户URL
    title = driver.find_elements_by_css_selector(".company-list-item .list-item-title .a::attr(href)")

    for i in len(title):
        #https://shop1481648000066.1688.com
        #进行URL合并，将匹配出来的与联系方式页面的URL进行合并
        contact_url = urljoin(title[i],"/page/contactinfo.htm?")
        #对商户联系方式页面进行请求
        response = urllib.request.urlopen(contact_url,headers = {'User-Agent': ua.ramdom})
        #
        html = response.text
        #对返回页面数据进行分析，提取公司名称、联系方式、地址






