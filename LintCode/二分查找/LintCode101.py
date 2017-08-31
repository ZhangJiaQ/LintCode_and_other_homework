删除排序数组中的重复数字 II 
跟进“删除重复数字”：
如果可以允许出现两次重复将如何处理？

样例

解题思路：在删除排序数组中的重复数字的基础上，设置一个count，如果当前数字出现超过两次则count = 0，不能再留下该数字


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        
        k = 0
        count = 1
        for i in range(1,len(A)):
            if A[i] != A[k]:
                k+=1
                A[k] = A[i]
                count = 1
            elif A[i] == A[k] and count > 0:
                k+=1
                A[k] = A[i]
                count -= 1
                
        del A[k+1:len(A)]
        return len(A)