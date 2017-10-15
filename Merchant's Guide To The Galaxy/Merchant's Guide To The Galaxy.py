import re


def parser(str):


    # 星际语言转换为罗马字符的字典
    star_to_roma = {}
    # 金属价格字典
    metal_price = {}
    content_array = str.split('\n')

    for i in content_array:
        # 将文章分成三种类型进行解析

        # 第一种句型，分析后完成星际语言与罗马数字转换字典
        if re.search(r'is [A-Z]', i):
            try:
                star_to_roma[i.split(' is ')[0]] = i.split(' is ')[1]
            except:
                print("请检查此行是否输入有误：{0}".format(i))

        # 第二种句型，分析后可以将星际语言转换为罗马数字后，求出金属的Credit价格
        elif re.search(r'is \d+', i):
            m = re.match(r'([a-z ]+[a-z]) ([A-Z][a-z]+) is (\d+) Credits', i)
            s = ''

            for k in m.group(1).split(" "):
                s += star_to_roma[k]
                # 构成罗马字符串，交给罗马字符串处理函数去处理
            try:
                metal_price[m.group(2)] = int(m.group(3)) / transform_roman_num2_alabo(s)
            except:
                print('{0}中有字符不属于罗马字符'.format(s))

        # 第三种句型，分析后可以解析问题，求出答案。
        elif re.search(r'how', i):

            # 对how many类的问题进行分析，匹配出对应信息
            if re.search('how much', i):
                star_str = re.match(r'how much is ([a-z ]+[a-z]) ?', i)
                try:
                    star_str_array = star_str.group(1).split(' ')
                    roma_str = ''
                    for i in star_str_array:
                        roma_str += star_to_roma[i]
                    print(star_str.group(1), 'is', transform_roman_num2_alabo(roma_str))
                except:
                    print("请检查此行是否输入有误：{0}".format(i))

            # 对how many类的问题进行分析，匹配出对应信息
            elif re.search('how many', i):
                star_str = re.match(r'how many Credits is (([a-z ]+[a-z]) ([A-Z][a-z]+)) ?', i)
                try:
                    star_str_array = star_str.group(2).split(' ')
                    roma_str = ''
                    for i in star_str_array:
                        roma_str += star_to_roma[i]
                    print(star_str.group(1), 'is', transform_roman_num2_alabo(roma_str) * metal_price[
                        star_str.group(3)], 'Credits')
                except:
                    print("请检查此行是否输入有误：{0}".format(i))

        else:
            print("请检查一下这行输入是否有误：{0}\n程序停止运行".format(i))
            break


def transform_roman_num2_alabo(roma_str):
    '''
    将罗马数字转化为阿拉伯数字
    '''
    roma_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if roma_str=='0':
        return 0
    else:
        res=0
        for i in range(0,len(roma_str)):
            if i==0 or roma_dict[roma_str[i]]<=roma_dict[roma_str[i-1]]:
                res+=roma_dict[roma_str[i]]
            else:
                res+=roma_dict[roma_str[i]]-2*roma_dict[roma_str[i-1]]
        return res


if __name__ == '__main__':
    with open(r'test.txt') as f:
        str = f.read()
        parser(str)



