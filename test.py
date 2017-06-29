import requests
#
# from selenium import webdriver
#
# url = '/home/judge/Desktop/23.htm'
#
# driver = webdriver.Firefox()
#
# driver.get('file:///home/judge/Desktop/23.htm')
#
# title = driver.find_elements_by_css_selector("a[class=list-item-title-text]")
# for i in range(len(title)):
#     contact_url = title[i].get_attribute("href")+'page/contactinfo.htm'
#     print (contact_url)
#
# contact_urlfrom urllib3.connectionpool import xrange
#
# for i in xrange(1, 100):
#     next_url = "https://s.1688.com/company/company_search.htm?sortType=pop&pageSize=30&keywords=%BE%C6&offset=3&beginPage={0}".format(i)
#     print (next_url)
#
#
#
# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.random)


# import time
#
# from selenium import webdriver
# from fake_useragent import UserAgent
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Firefox()
#
# time.sleep(3)
# # 商户页面的URL
# # https://s.1688.com/company/company_search.htm?keywords=%BE%C6&n=y&spm=a260k.635.1998096057.d1
# url = 'https://s.1688.com/company/company_search.htm?keywords=%BE%C6'
# # 登录的url
# login_url = 'https://login.taobao.com/member/login.jhtml'
# # 跳转到登录页面
# driver.get(login_url)
# driver.maximize_window()
# # 睡眠5秒
# time.sleep(5)
#
# # 利用selenium的find_element方法选择帐号密码然后进行登录
# element = WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath("//*[@id='J_Quick2Static']"))
# element.click()
# driver.find_element_by_name("TPL_username").send_keys('3382315515@qq.com')  # 3382315515@qq.com  zmq2007zz
# driver.find_element_by_name("TPL_password").clear()
# driver.find_element_by_name("TPL_password").send_keys('zmq2006zz')  # zmq2006zz   2zhlmcl
# driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
# time.sleep(30)
#
# # 跳转到化工商户页面的url
# driver.get(url)
# # 防爬虫的UserAgent处理
# ua = UserAgent()
# title = driver.find_elements_by_css_selector("a[class=list-item-title-text]")
# contact_url = title[0].get_attribute("href") + 'page/contactinfo.htm'
# cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
# print (cookie)
# cookiestr = ';'.join(item for item in cookie)
# print (cookiestr)
# print (contact_url)
# cookies={}#初始化cookies字典变量
# for line in cookiestr.split(';'):   #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     name,value=line.strip().split('=',1)
#     cookies[name]=value
#
# headers = {'User-Agent': ua.random,
#            'Accept': '*/*',
#            'Referer': 'http://www.google.com',
#            }
# r = requests.get(contact_url, headers=headers,cookies=cookies)
# print (r.status_code,"\n",r.text)
#

# str = 'JSESSIONID=8L78bDuu1-bHwXPkJBCHzxC97ww8-xSsekNQ-WZR;ad_prefer="2017/06/27 20:30:34";h_keys="%u9152";_tmp_ck_0="AhAPwLGenDvWkaiBDceLNcdBNldxSA%2B0dij8m7Kr3ocjlsCdTBH6KRSzKPSM9BBsvcNV5B40gMLLdHeQFUWaRtVqgY0KKHROFS%2FbH45svSF9w44zq03NpnXWh7lkt4rtdGF9H7SRYIFNJuMxAuwG52nwwykGa3sq5kRlTRO%2FebTSveBJxAthjf8fBReifIlG%2B%2FfFo4cAgBKOgtCPnLyrNpyl3a%2BrUkpe4YyzX9NMlOqZ95XaS82fRdAgvZ8q%2FpZ8JlEL0NnbmyxIX%2Baq%2F5Di%2FWflL7XZyXJa1o8E0fPzPaLA%2BhPuZidGd6cGG0ktSpfAdH52aE9fZvHwvswx4EUq9Q%3D%3D";alisw=swIs1200%3D1%7C;cna=xT3ZEWyb+VUCATrVcMOVX76l;ali_ab=58.213.112.195.1498566634961.1;__cn_logon_id__=zmq2007zz;__last_loginid__=zmq2007zz;__cn_logon__=true;last_mid=b2b-168444220;alicnweb=touch_tb_at%3D1498566636886'
#
# cookies={}#初始化cookies字典变量
# for line in str.split(';'):   #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     name,value=line.strip().split('=',1)
#     cookies[name]=value
# print (cookies)


import re
from bs4 import BeautifulSoup
member_name_pattern = re.compile('<a.*?class="membername".*?>(.*?)</a>', re.S)
address_pattern = re.compile('"address">(.*?)</dd>', re.S)
pattern = re.compile('<div class="contcat-desc".*?>(.*?)</div>', re.S)

with open('/home/judge/Desktop/4567.html','r') as f:
    soup = BeautifulSoup(f.read(),"html.parser")

    phone_html = soup.find(class_='m-mobilephone')
    phone_num_match = re.match(r'\D*(\d+).*',str(phone_html),re.DOTALL)
    if phone_num_match:
        phone_num = int(phone_num_match.group(1).replace(" ",""))
    else:
        phone_num = 0

    name_html = soup.find(class_='contact-info').h4
    name_content_match = re.match(r'.*<h4>(.*)</h4>.*',str(name_html),re.DOTALL)
    if name_content_match:
        name_content = name_content_match.group(1).replace(" ","")
    else:
        name_content = ''

    address_html = soup.find(class_='address')
    address_content_match = re.match(r'.*s">(.*?)</dd>*', str(address_html), re.DOTALL)
    if address_content_match:
        address_content = address_content_match.group(1).replace(" ","")
    else:
        address_content = ''

    print(address_content,name_content,phone_num)
