import time
import requests
import re

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
driver.find_element_by_name("TPL_username").send_keys('***')#***
driver.find_element_by_name("TPL_password").clear()
driver.find_element_by_name("TPL_password").send_keys('***')#***
driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()

#异地登录，需要输入手机验证码
time.sleep(30)

# 跳转到化工商户页面的url
driver.get(url)

# 防爬虫的UserAgent处理
ua=UserAgent()

#利用Selunium将Cookie保存下来，便于Requests使用
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookiestr = ';'.join(item for item in cookie)
cookies={}
for line in cookiestr.split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value

#进行数据爬取
for page in range(1, 100):
    #选择爬取每个商户主页的URL
    title = driver.find_elements_by_css_selector("a[class=list-item-title-text]")
    #爬取每个商户联系方式页面，并解析提取
    for i in range(len(title)):
        contact_url = title[i].get_attribute("href") + 'page/contactinfo.htm'
        #print(contact_url)
        headers = {'User-Agent': ua.random, 'Accept': '*/*', 'Referer': 'http://www.google.com'}
        r = requests.get(contact_url, headers=headers, cookies=cookies)
        contact_content = r.text
        soup = BeautifulSoup(r.text, "html.parser")

        phone_html = soup.find(class_='m-mobilephone')
        phone_num_match = re.match(r'\D*(\d+).*', str(phone_html), re.DOTALL)
        if phone_num_match:
            phone_num = int(phone_num_match.group(1))
        else:
            phone_num = 0

        name_html = soup.find(class_='contact-info').h4
        name_content_match = re.match(r'.*<h4>(.*)</h4>.*', str(name_html), re.DOTALL)
        if name_content_match:
            name_content = name_content_match.group(1)
        else:
            name_content = ''

        address_html = soup.find(class_='address')
        address_content_match = re.match(r'.*s">(.*?)</dd>*', str(address_html), re.DOTALL)
        if address_content_match:
            address_content = address_content_match.group(1)
        else:
            address_content = ''

        print(address_content, '\n', name_content, '\n', phone_num)
        pass

    #进行下一页的爬取
    next_url = "https://s.1688.com/company/company_search.htm?sortType=pop&pageSize=30&keywords=%BE%C6&offset=3&beginPage={0}".format(i)
    driver.get(next_url)



