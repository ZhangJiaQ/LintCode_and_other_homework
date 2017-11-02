# coding: utf-8
import time
import requests
import xlrd


def reader():
    test_url = []
    test_method = []
    test_input = []
    data = xlrd.open_workbook('setting.xlsx')
    table = data.sheets()[0]
    need_login = str(table.cell(0,1).value)
    user = str(int(table.cell(1,1).value))
    pwd = str(int(table.cell(1,2).value))
    login_url = str(table.cell(1,3).value)
    for i in range(5, table.nrows):
        test_url.append(str(table.row_values(i)[0]))
        test_method.append(str(table.row_values(i)[1]))
        test_input.append(str(table.row_values(i)[2]))
    return need_login, user, pwd, test_input, test_method, test_url, login_url


def connecter(need_login, user, pwd, test_input, test_method, test_url, login_url):
    cookies = {}
    result = []
    if need_login:
        r = requests.post(login_url, params={'username':user, 'password':pwd})
        if r.status_code == 200:
            cookies = r.cookies
        else:
            print('需要登录但登录失败')
            return
    for i in range(len(test_url)):
        if test_method[i].upper() == 'GET':
            #get
            r = requests.get(test_url[i], params=test_input[i], cookies=cookies)
            if r.status_code == 200:
                result.append(r.json())
            else:
                result.append(r.status_code)
        elif test_method[i].upper() == 'POST':
            #post
            r = requests.post(test_url[i], params=test_input[i], cookies=cookies)
            if r.status_code == 200:
                result.append(r.json())
            else:
                result.append(r.status_code)

    return result, test_url, test_input


def write(result, test_url, test_input):

    if result and len(result):
        with open('{0}.txt'.format(str(time.time())), 'w') as f:
            for i in range(min(len(result), len(test_url))):
                f.write(test_url[i])
                f.write('\n')
                f.write(test_input[i])
                f.write('\n')
                f.write(str(result[i]))
                f.write('\n\n')
        print('OK')
    else:
        print('wrong')
        return


if __name__ == '__main__':
    need_login, user, pwd, test_input, test_method, test_url, login_url = reader()
    result = connecter(need_login, user, pwd, test_input, test_method, test_url, login_url)
    write(result, test_url, test_input)
