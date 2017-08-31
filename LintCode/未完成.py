移动零 
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

样例
给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].

解题思路： 两根指针，一根计算偏移量，如果数组元素值等于0偏移量加一，不等于零数组向左偏移（偏移量）个单位
		   最后数组后偏移量个单位全为0即可

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        j = 0
        for k in range(0,len(nums)):
            if nums[k] == 0:
                j += 1
            else:
                nums[k-j] = nums[k]
        
        for i in range(len(nums)-j,len(nums)):
            nums[i] = 0
    
        return nums       