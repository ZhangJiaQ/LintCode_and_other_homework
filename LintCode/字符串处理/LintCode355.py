'''查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：

前2个数是 0 和 1 。
第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...'''


'''
解题思路
1.使用递归方式，	Runtime Error,
2.使用非递归方式，将N个数转换为长度为N的数组，取第N个值
'''

class Solution:
    """
    @param: : an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        num = [0,1]
        if n == 1:
            return 0
        if n == 2:
            return 1
        for n in range(0,n-2):
            num.append(num[-1]+num[-2])
        return num[-1]