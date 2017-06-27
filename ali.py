import time
import requests

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
driver.find_element_by_name("TPL_username").send_keys('zmq2007zz')#3382315515@qq.com
driver.find_element_by_name("TPL_password").clear()
driver.find_element_by_name("TPL_password").send_keys('2zhlmcl,')#zmq2006zz
driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
time.sleep(30)

# 跳转到化工商户页面的url
driver.get(url)
# 防爬虫的UserAgent处理
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
ua=UserAgent()
cookiestr = ';'.join(item for item in cookie)

for page in range(1, 100):
    #
    title = driver.find_elements_by_css_selector("a[class=list-item-title-text]")

    for i in range(len(title)):
        contact_url = title[i].get_attribute("href") + 'page/contactinfo.htm'
        #print(contact_url)
        headers = {'User-Agent': ua.random, 'Accept': '*/*', 'Referer': 'http://www.google.com'}

    #
    next_url = "https://s.1688.com/company/company_search.htm?sortType=pop&pageSize=30&keywords=%BE%C6&offset=3&beginPage={0}".format(i)
    driver.get(next_url)



