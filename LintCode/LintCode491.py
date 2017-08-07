# 回文数 
# 判断一个正整数是不是回文数。
# 回文数的定义是，将这个数反转之后，得到的数仍然是同一个数。
# 样例
# 11, 121, 1, 12321 这些是回文数。
# 23, 32, 1232 这些不是回文数。

# 解题思路：将数字转换为字符串，然后将字符串翻转与源字符串进行对比

class Solution:
    # @param {int} num a positive number
    # @return {boolean} true if it's a palindrome or false
    def palindromeNumber(self, num):
        # Write your code here
        s = str(num)
        if s[::-1] == s:
            return True
        else:
            return False