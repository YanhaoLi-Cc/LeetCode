#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        # merged = []
        # for interval in intervals:
        #     if not merged:
        #         merged.append(interval)
        #     if merged[-1][1] < interval[0]:
        #         merged.append(interval)
        #     else:
        #         merged[-1][1] = max(merged[-1][1], interval[1])
        # return merged
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        left, right = intervals[0][0], intervals[0][1]
        
        for interval in intervals:
            if right >= interval[0]:
                if right > interval[1]:
                    continue
                else:
                    right = interval[1]
            else:
                merged.append([left, right])
                left, right = interval[0], interval[1]
        return merged + [[left, right]]
# @lc code=end

