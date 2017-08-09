# 有效回文串 
# 给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。
# 样例
# "A man, a plan, a canal: Panama" 是一个回文。
# "race a car" 不是一个回文。

# 解题思路：由于需要忽略标点与空格，只对字母和数字进行回文判定，所以我们需要先对字符串进行处理，遍历字符串并使用
		  # isalpha()方法与isnumeric()方法取得字母与数字，然后将字母全变为小写，进行回文判定。

class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        new_string = ''
        for i in s:
            if i.isalpha() or i.isnumeric():
                new_string += i
        if new_string.lower() == new_string.lower()[::-1]:
            return True
        else:
            return False