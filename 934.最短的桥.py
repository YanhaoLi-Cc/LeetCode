#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
# from collections import deque
# from itertools import pairwise

# class Solution:    
#     def shortestBridge(self, grid: list[list[int]]) -> int:
#         def dfs(i, j):
#             q.append((i, j))
#             grid[i][j] = -1
            
#             for a, b in pairwise(dirs):
#                 x, y = i + a, j + b
#                 if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
#                     dfs(x, y)
                    
#         n = len(grid)
#         dirs = (-1, 0, 1, 0, -1)
#         q = deque()
#         i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
#         dfs(i, j)
#         ans = 0
        
#         while True:
#             for _ in range(len(q)):
#                 i, j = q.popleft()
#                 for a, b in pairwise(dirs):
#                     x, y = i + a, j + b
#                     if 0 <= x < n and 0 <= y < n:
#                         if grid[x][y] == 1:
#                             return ans
#                         if grid[x][y] == 0:
#                             grid[x][y] = -1
#                             q.append((x, y))
#             ans += 1

from collections import deque
from itertools import product
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])  # 获取网格的行数和列数
        q = deque()  # 用于广度优先搜索的队列
        
        # 1. 找到第一个岛屿并将其所有坐标入队列，同时使用集合 s 存储已访问节点
        for i, j in product(range(n), range(m)):
            if grid[i][j]:  # 如果找到陆地
                q.append((i, j, 0))  # 将该位置入队，步数初始化为 0
                s = set([(i, j)])  # 初始化集合 s，存储已访问节点
                break  # 找到第一个岛屿后退出循环
        
        # 2. 扩展第一个岛屿边界，寻找与第二个岛屿的最短连接
        while q:
            x, y, step = q.popleft()  # 从队列中取出当前节点及其步数

            # 遍历当前节点的四个方向
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy  # 计算新位置

                # 确保新位置在网格范围内，并且未访问过
                if 0 <= nx < n and 0 <= ny < m and ((nx, ny) not in s):
                    s.add((nx, ny))  # 标记新位置为已访问

                    # 若新位置是陆地（即遇到第二个岛屿）
                    if grid[nx][ny] == 1:
                        if step:
                            return step  # 若步数非零，说明已扩展过水域，返回步数
                        q.appendleft((nx, ny, 0))  # 否则，将新位置作为第一个岛屿扩展
                    else:
                        q.append((nx, ny, step + 1))  # 若新位置是水域，步数加 1
        
        return 0  # 如果没有找到第二个岛屿，返回 0

# @lc code=end


sol = Solution()
grid = [[0,1,0],[0,0,0],[0,0,1]]

sol.shortestBridge(grid)
