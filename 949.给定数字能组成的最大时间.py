#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#

# @lc code=start
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # itertools.permutations
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(arr):
            hours = h1 * 10 + h2
            mins = m1 * 10 + m2
            times = hours * 60 + mins
            if hours < 24 and mins < 60 and times > ans:
                ans = times
        if ans == -1:
            return ""

        return "{:02}:{:02}".format(ans//60, ans%60)

# @lc code=end

