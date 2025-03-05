#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        kk = k % len(nums)

        nums[:] = nums[len(nums)-kk:] + nums[:len(nums)-kk] 
        
# @lc code=end

