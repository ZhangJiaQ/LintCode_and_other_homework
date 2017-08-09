# 翻转字符串 
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 说明
# 单词的构成：无空格字母构成一个单词
# 输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
# 如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个

# 样例 A = ‘how are you?’   返回 'you? are how'

# 解题思路：直接对字符串进行split以space为参数进行分割，分割得到的字符串进行倒叙遍历，添加到返回字符串中，每添加一个字符串加一个空格，
		  # 最后对处理好的字符串进行右端空格的处理，返回字符串

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        s_none_space = s.lstrip().rstrip() # 多余，可以去掉
        s_array = s_none_space.split(' ')
        s_reverse = ''
        for i in range(len(s_array)-1,-1,-1):
            if len(s_array[i]) != 0:
                s_reverse += s_array[i]
                s_reverse += ' '
                
        s_reverse = s_reverse.rstrip()
        return s_reverse