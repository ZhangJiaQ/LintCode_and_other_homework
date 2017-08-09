判断字符串是否没有重复字符 
实现一个算法确定字符串中的字符是否均唯一出现
样例
给出"abc"，返回 true
给出"aab"，返回 false

解题思路：使用set去重后比较长度

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        if len(set(str)) == len(str):
            return True
        else:
            return False