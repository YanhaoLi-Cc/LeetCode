#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # n = len(triangle)
        # f = [[0]*n for _ in range(n)]
        # f[0][0] = triangle[0][0]
        
        # for i in range(1, n):
        #     f[i][0] = f[i - 1][0] + triangle[i][0]
        #     for j in range(1, i):
        #         f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        #     f[i][i] = f[i - 1][i - 1] + triangle[i][i]
            
        # return min(f[n - 1])
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        return triangle[0][0]
# @lc code=end

