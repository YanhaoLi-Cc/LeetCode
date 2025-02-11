#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations = sorted(citations, reverse=True)
        # h = 0
        # for i in range(len(citations)):
        #     if citations[i] > h:
        #         h += 1
        # return h
        left, right = 0, len(citations)
        while left < right:
            mid = (left + right + 1) // 2
            cnt = 0
            for cit in citations:
                if cit >= mid:
                    cnt += 1
            if cnt >= mid:
                left = mid
            else:
                right = mid - 1
        return left
# @lc code=end

