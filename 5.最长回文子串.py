#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # length = len(s)
        # if length < 2:
        #     return s
    
        # max_len = 1
        # begin = 0
        
        # dp = [[False]*length for _ in range(length)]
        # for i in range(length):
        #     dp[i][i] = True
            
        # # 递推开始
        # # 先枚举子串长度
        # for n in range(2, length + 1):
        #     for l in range(length):
        #         # j - i + 1 = L 
        #         r = l + n - 1
        #         # 防止越界
        #         if r >= length:
        #             break
                
        #         if s[l] != s[r]:
        #             dp[l][r] = False
        #         else:
        #             if r - l < 3:
        #                 dp[l][r] = True
        #             else:
        #                 dp[l][r] = dp[l + 1][r - 1]

        #         if dp[l][r] and r - l + 1 > max_len:
        #             max_len = r - l + 1
        #             begin = l
                    
        # return s[begin:begin + max_len]
        
        # 中心扩展法
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]
        
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
# @lc code=end

sol = Solution()
print(sol.longestPalindrome("abcba"))