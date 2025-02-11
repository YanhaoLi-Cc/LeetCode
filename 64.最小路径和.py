#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             continue
        #         elif i == 0:
        #             grid[i][j] += grid[i][j-1]
        #         elif j == 0:
        #             grid[i][j] += grid[i-1][j]
        #         else:
        #             grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # return grid[m - 1][n - 1]
        m, n = len(grid), len(grid[0])
        MAX = 1e8
        dp = [[MAX] * (n + 1) for _ in range((m + 1))]
        dp[0][1] = dp[1][0] = 0
        
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        
        return dp[m][n] 
# @lc code=end

