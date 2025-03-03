#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, self.dfs(i, j, grid))
        return ans

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        ans = 1
        grid[i][j] = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for di, dj in dirs:
            ans += self.dfs(i + di, j + dj, grid)
        return ans
    
     
# @lc code=end

