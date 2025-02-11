#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#

# @lc code=start
from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n)) # 三个属性分别为 idx, mask, dist；存入起点, 标记, 起始距离0
        vis = {(i, 1 << i) for i in range(n)} # 节点编号及当前状态
        
        while q:
            x, mask, 
        
# @lc code=end


sol = Solution()
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
sol.shortestPathLength(graph)