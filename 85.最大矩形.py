#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    # def maximalRectangle(self, matrix) -> int:
        # m, n = len(matrix), len(matrix[0])
        # # 记录当前位置上方连续1的个数
        # dp = [[0] * (n + 1) for _ in range(m)]
        # maxAns = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == '1':
        #             if i == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = dp[i - 1][j] + 1
        #         else:
        #             dp[i][j] = 0
                    
        #     stack = [-1]
        #     for k in range(n + 1):
        #         while stack and dp[i][stack[-1]] > dp[i][k]:
        #             h = dp[i][stack.pop()]
        #             w = k - stack[-1] - 1
        #             maxAns = max(maxAns, h * w)
        #         stack.append(k)
        # return maxAns
    
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left_j = [-1] * n
        right_j = [n] * n
        height = [0] * n
        maxArea = 0
        for i in range(m):
            cur_left = -1
            cur_right = n
            
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for j in range(n):
                if matrix[i][j] == '1':
                    left_j[j] = max(left_j[j], cur_left)
                else:
                    left_j[j] = -1
                    cur_left = j
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right_j[j] = min(right_j[j], cur_right)
                else:
                    right_j[j] = n
                    cur_right = j
            
            for j in range(n):
                maxArea = max(maxArea, height[j] * (right_j[j] - left_j[j] - 1))
        return maxArea
# @lc code=end


sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))