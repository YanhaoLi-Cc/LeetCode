#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
#         # 构建邻接矩阵
#         g = [[1e6] * n for _ in range(n)]
#         for x, y, time in times:
#             g[x - 1][y - 1] = time
            
#         # 初始化最短距离数组和已访问标记数组
#         distance = [1e6] * n
#         distance[k - 1] = 0
#         used = [False] * n
        
#         # 执行 Dijkstra 算法
#         for _ in range(n):
#             x = -1 
#             for y, u in enumerate(used):
#                 if not u and (x == -1 or distance[y] < distance[x]):
#                     x = y
                
#             if x == -1:
#                 break
#             used[x] = True
#             for y, time in enumerate(g[x]):
#                 distance[y] = min(distance[y], distance[x] + time)
            
#         ans = max(distance)
#         return -1 if ans == 1e6 else ans

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 构建邻接表
        dct = defaultdict(dict)
        for u, v, w in times:
            dct[u][v] = w

        # 初始化访问数组和优先队列
        visit = [-1] * n
        stack = [[0, k]]
        
        # Dijkstra算法
        while stack:
            time, i = heapq.heappop(stack)
            if visit[i - 1] != -1:
                continue
            visit[i - 1] = time
            for j in dct[i]:
                heapq.heappush(stack, [time + dct[i][j], j])
        
        # 检查是否所有节点都访问过
        if min(visit) == -1:
            return -1
        return max(visit)



# @lc code=end

