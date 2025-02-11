#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
@cache
def dp(i, j):
    if i == 0:
        return inf if j else 0
    if i*i > j:
        return dp(i-1, j)

    return min(dp(i-1,j), dp(i, j-i*i) + 1)

class Solution:
    def numSquares(self, n: int) -> int:
        return dp(isqrt(n), n)
# @lc code=end

