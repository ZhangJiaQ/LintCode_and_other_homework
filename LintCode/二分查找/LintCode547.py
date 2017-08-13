# 两数组的交 
# 返回两个数组的交
 # 注意事项
# Each element in the result must be unique.
# The result can be in any order.

 # 样例nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2]
 
 # 解题思路：先将数组set(),使数组元素唯一，再对数组进行排序，使用两个指针遍历数组
 
 class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
	
        if nums1 == None or nums2 == None:
            return []
        result = []
        i,j=0,0
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        
        while i < len(nums1) and j < len(nums2):
            while i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
                i += 1
            while j < len(nums2) and i < len(nums1) and nums2[j] < nums1[i]:
                j += 1
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                    result.append(nums2[j])
                    i += 1
                    j += 1
        
        return result
        