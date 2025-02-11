#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        UnlyList = [1]
        i2, i3, i5 = 0, 0, 0
        while len(UnlyList) < n:
            min_val = min(UnlyList[i2] * 2, UnlyList[i3] * 3, UnlyList[i5] * 5)
            UnlyList.append(min_val)
            
            if min_val == UnlyList[i2] * 2:
                i2 += 1
            if min_val == UnlyList[i3] * 3:
                i3 += 1
            if min_val == UnlyList[i5] * 5:
                i5 += 1
        return UnlyList[n - 1]
    
# @lc code=end

