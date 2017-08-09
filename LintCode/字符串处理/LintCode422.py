最后一个单词的长度 

给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

样例
给定 s = "Hello World"，返回 5。

解题思路：1、先使用python去空格及特殊符号函数s.strip().lstrip().rstrip(',')对字符串右端进行去空格
		  2、再使用分割字符串s.split(' ')，对字符串进行分割，返回分割好的数组中第[-1]个字符串的长度
		  
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        t = s.rstrip(' ')
        return len(t.split(' ')[-1])