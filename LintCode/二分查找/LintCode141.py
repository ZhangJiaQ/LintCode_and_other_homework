x的平方根 
实现 int sqrt(int x) 函数，计算并返回 x 的平方根

样例
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(10) = 3

解题思路：使用二分搜索，确定平方根的位置 返回

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        if x == 1:
            return 1
        low,high = 0,x
        
        while low < high:
            mid = (low+high) // 2
            
            if mid * mid == x:
                return mid
            if mid * mid <= x and (mid + 1)*(mid + 1) > x:
                return mid
            if mid * mid > x and (mid - 1)*(mid - 1) <= x:
                return mid - 1
                
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1