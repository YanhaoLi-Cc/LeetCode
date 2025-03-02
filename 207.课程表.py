#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        未被 DFS 访问：flag[i] == 0；
        已被其他节点启动的 DFS 访问：flag[i] == -1；
        已被当前节点启动的 DFS 访问：flag[i] == 1
        
        终止条件：
            当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，直接返回 True。
            当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环 ，直接返回 False。

            https://leetcode.cn/problems/course-schedule/solutions/18806/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
        '''
        adj = [[] for _ in range(numCourses)]
        flag = [0 for _ in range(numCourses)]

        def dfs(i, adj, flag):
            if flag[i] == -1: return True
            if flag[i] == 1: return False
            flag[i] = 1
            for j in adj[i]:
                if not dfs(j, adj, flag):
                    return False
            flag[i] = -1
            return True
            
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adj, flag):
                return False
        return True


# @lc code=end

