# 空格替换 
# 设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。
# 你的程序还需要返回被替换后的字符串的长度。

# 样例
# 对于字符串"Mr John Smith", 长度为 13
# 替换空格之后，参数中的字符串需要变为"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。

# 解题思路：1）注意字符串类型为数组类型
		  # 2）对字符串数组进行判定，如果遇见space值，使用.remove将space值移除，添加'%','2','0'三个值
		  # 3）对length不断进行更新，因为数组长度在不断变化，循环判定为超过数组长度停止循环

class Solution(object):
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string, length):
        if string == None:
            return 0
        i = 0
        length = len(string)
        while i < length:
            if string[i] == ' ':
                string.remove(string[i])
                string.insert(i, '%')
                string.insert(i+1, '2')
                string.insert(i+2, '0')
            i += 1
            length = len(string)

        return length