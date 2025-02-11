#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max = nums[0]
        pre_min = nums[0]
        ansMax = nums[0]
        for i in nums[1:]:
            cur_max = max(pre_max * i, pre_min * i, i)
            cur_min = min(pre_max * i, pre_min * i, i)
            ansMax = max(ansMax, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return ansMax
            
# @lc code=end

