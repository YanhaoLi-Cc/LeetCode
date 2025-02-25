#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 每次只考虑新腐烂的橘子（new_rotten）而不是所有腐烂的橘子（rotten）
        m, n = len(grid), len(grid[0])

        rotten = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}

        times = 0

        while fresh:
            if not rotten:
                return -1
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            new_rotten = set()
            for i, j in rotten:
                for di, dj in direction:
                    if (i + di, j + dj) in fresh:
                        new_rotten.add((i + di, j + dj))
                        
            rotten = new_rotten
            times += 1
            fresh -= rotten

        return times
        

                    
                       
# @lc code=end