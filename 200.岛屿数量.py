#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS 把根据（i, j）能遍历到的岛屿都设置为0
        """
        def dfs(grid, i, j):
            if grid[i][j] == "0":
                return    

            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i - 1 >= 0: 
                    dfs(grid, i - 1, j)
                if j - 1 >= 0:
                    dfs(grid, i, j - 1)
                if i + 1 < m:
                    dfs(grid, i + 1, j)
                if j + 1 < n:
                    dfs(grid, i, j + 1)
            
        
        nums = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    nums += 1
                    dfs(grid, i, j)
                    
        return nums

  
# @lc code=end

