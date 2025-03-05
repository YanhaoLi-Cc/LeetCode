#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和字典，key是前缀和，value是该前缀和出现的次数
        prefix_sum = {0: 1}
        count = 0
        cur_sum = 0
        m = len(nums)
        for i in range(m):
            # 计算当前的前缀和
            cur_sum += nums[i]

            # 计算需要寻找的前缀和
            target_sum = cur_sum - k

            # 如果目标前缀和存在于字典中，增加计数
            if target_sum in prefix_sum:
                count += prefix_sum[target_sum]
            
            if cur_sum in prefix_sum:
                prefix_sum[cur_sum] += 1
            else:
                prefix_sum[cur_sum] = 1
        
        return count
# @lc code=end

