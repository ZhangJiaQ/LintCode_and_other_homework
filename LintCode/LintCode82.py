#落单的数 

#给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

#解题思路 使用或运算，求得多出来的那个数字

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if len(A)==0:
            return 0
        n=A[0]
        for i in range(1,len(A)):
            n=n^A[i]
        return n 