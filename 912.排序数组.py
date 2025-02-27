#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(start, end):
            if start >= end:
                return
            
            pivot = nums[start]
            left, right = start, end
        
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left] <= pivot:
                     left += 1
                nums[right] = nums[left]

            nums[left] = pivot

            quick_sort(start, left - 1)
            quick_sort(left + 1, end)

        return quick_sort(0, len(nums)-1)
# @lc code=end

