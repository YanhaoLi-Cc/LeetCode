#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)

        L = [0 for _ in range(m)]
        L[0] = 1

        R = [0 for _ in range(m)]
        R[m - 1] = 1

        ans = [0 for _ in range(m)]

        for i in range(1, m):
            L[i] = L[i - 1] * nums[i - 1]
        for i in range(m - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(m):
            ans[i] = L[i] * R[i]
        return ans
        

# @lc code=end


nums = [1,2,3,4] 
sol = Solution()
sol.productExceptSelf(nums)