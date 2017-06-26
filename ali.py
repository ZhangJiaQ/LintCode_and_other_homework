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
# 商户页面的url
# https://s.1688.com/company/company_search.htm?keywords=%BE%C6&n=y&spm=a260k.635.1998096057.d1
url = 'https://s.1688.com/company/company_search.htm?keywords=%BE%C6&button_click=top&earseDirect=false&n=y'
# 登录的url
login_url = 'https://login.taobao.com/member/login.jhtml'
# 跳转到登录页面
driver.get(login_url)
# 睡眠5秒
time.sleep(5)
#
driver.find_element_by_css_selector("@TPL_username_1").send_keys("*******")
driver.find_element_by_css_selector("@TPL_password_1").send_keys('*******码')
driver.find_element_by_css_selector("@J_SubmitStatic").click()
# 睡眠5秒
time.sleep(5)
# 跳转到化工商户页面的url
driver.get(url)

ua=UserAgent()

for page in xrange(1, 100):
    #
    title = driver.find_elements_by_css_selector(".company-list-item .list-item-title .a::attr(href)")

    for i in len(title):
        #https://shop1481648000066.1688.com
        contact_url = urljoin(title[i],"/page/contactinfo.htm?")

        response = urllib.request.urlopen(contact_url,headers = {'User-Agent': ua.ramdom})

        html = response.text






