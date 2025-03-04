#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        哎 Tencent挂了 我是SB
        """
        i, j = 0, 0
        nums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < m:
            nums += nums1[i:m]
        if j < n:
            nums += nums2[j:n]

        nums1[:] = nums
        
# @lc code=end

