二分查找 
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
样例
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。

解题思路：利用二分查找，将查找范围缩小到长度为2，对这两个数进行查询返回相应的值

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid
            else:
                high = mid

        if target == nums[low]:
            return low
        if target == nums[high]:
            return high

        return False