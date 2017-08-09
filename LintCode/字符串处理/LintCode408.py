# 二进制求和
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 样例
# a = 11
# b = 1
# 返回 100

# 解题思路：利用bin()与int()函数进行进制转换然后截取[2:]个元素，取得二进制的值

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        return bin(int(a,2)+int(b,2))[2:]