删除元素
给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。
元素的顺序可以改变，并且对新的数组不会有影响。

样例
给出一个数组 [0,4,4,0,0,2,4,4]，和值 4
返回 4 并且4个元素的新数组为[0,0,0,2]

解题思路： 设置两个指针，一个记录偏移量，一个对数组当前元素值进行判断。

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here】
        j = 0
        for k in range(0,len(A)):
            if A[k] == elem:
                j += 1
            else:
                A[k-j] = A[k]
                
        del A[len(A)-j:len(A)]
        return A