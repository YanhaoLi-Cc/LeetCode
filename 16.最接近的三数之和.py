#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 1e9
        
        for a in range(n):
            b, c = a+1, n-1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if s == target:
                    return target
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    b += 1
                else:
                    c -= 1
        return best
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         best = 1e9  # 初始化最优解
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     s = nums[i] + nums[j] + nums[k]
#                     if abs(s - target) < abs(best - target):
#                         best = s  # 更新最优解
#         return best
# @lc code=end

