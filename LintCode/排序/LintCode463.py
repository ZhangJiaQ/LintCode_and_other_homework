整数排序 
给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。

解题思路：冒泡排序

class Solution:
    """
    @param: A: an integer array
    @return: 
    """
    def sortIntegers(self, A):
        # write your code here
        if len(A) < 2:
            return A
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    A[i],A[j] = A[j],A[i]
        return A