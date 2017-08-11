# 经典二分查找问题 
# 在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1

# 样例
# 给出数组 [1, 2, 2, 4, 5, 5].
# 对于 target = 2, 返回 1 或者 2.
# 对于 target = 5, 返回 4 或者 5.
# 对于 target = 6, 返回 -1.

# 解题思路：采用二分搜索的办法进行遍历

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == A[mid]:
                return mid
            elif target > A[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1