删除排序数组中的重复数字 
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。

解题思路：在数组内使用两根指针，如果值相同的话第二根指针继续向前遍历，如果值不同第一个指针向前一次并和第二根指针指向的值进行交换


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        
        k = 0
        for i in range(1,len(A)):
            if A[i] != A[k]:
                k+=1
                A[k] = A[i]
                
        del A[k+1:len(A)]
        return len(A)