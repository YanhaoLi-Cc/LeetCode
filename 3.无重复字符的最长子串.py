#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        substr = set()

        for i in range(n):
            j = i
            while j < n and s[j] not in s[i:j]:
                substr.add(s[i:j + 1])
                j += 1

        longest_substr = len(max(substr, key=len)) if substr else 0
                
        return longest_substr
# @lc code=end

s = "abcabc"
sol = Solution()
sol.lengthOfLongestSubstring(s)