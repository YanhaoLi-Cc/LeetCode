#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 顺时针旋转90度后，原矩阵中的位置(i,j)应该对应到新矩阵的(j,n-i-1)位置
        n = len(matrix[0])
        copy = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                copy[j][n - i - 1] = matrix[i][j]
        for i in range(n):
            matrix[i] = copy[i]
# @lc code=end

