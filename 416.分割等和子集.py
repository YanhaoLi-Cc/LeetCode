#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i < 0:
                return True if j == 0 else False
            
            if j >= nums[i]:
                return dfs(i-1, j-nums[i]) or dfs(i-1, j)
            else:
                return dfs(i-1, j)

        if sum(nums) % 2 == 0:
            return dfs(len(nums) - 1, sum(nums) // 2)
        else:
            return False
            
        
# @lc code=end

