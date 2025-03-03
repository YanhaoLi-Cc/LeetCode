#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result = itertools.permutations(nums)
        # result = [list(item) for item in result]

        results = []
        def backtrack(current, remaining):
            if len(remaining) == 0:
                results.append(current[:])
                return
            
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()
        
        backtrack([], nums)
        
        return results


        
# @lc code=end

nums = [1,2,3]
sol = Solution()
sol.permute(nums)
