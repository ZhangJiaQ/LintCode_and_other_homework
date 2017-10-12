import re

str = '''glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?'''
#将文章分割为数组
content_array = str.split('\n')
#进行匹配，将文章数组分为三个部分
credit_pattern = re.compile('Credits')
how_pattern = re.compile('how')
i,j = 0, 0
#记录匹配值
for i in range(len(content_array)):
    if re.search(credit_pattern, content_array[i]):
        break
for j in range(len(content_array)):
    if re.search(how_pattern,content_array[j]):
        break
#分割完成三个数组
roma_array = content_array[:i]
credit_array = content_array[i:j]
question_array = content_array[j:]
#对第一个数组进行字典化，得出星际语言转为罗马数字的字典






