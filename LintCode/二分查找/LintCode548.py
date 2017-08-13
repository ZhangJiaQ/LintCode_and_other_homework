计算两个数组的交
 注意事项
每个元素出现次数得和在数组里一样
答案可以以任意顺序给出

样例 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

解题思路： 先将数组排序，再使用两个指针对数组进行遍历

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        
        if nums1 == None or nums2 == None:
            return []
        
        result = []
        i,j = 0,0
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
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