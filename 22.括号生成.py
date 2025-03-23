#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s="", left_count=0, right_count=0):
            if len(s) == 2 * n:
                ans.append(s)
                return 
            # 如果开括号数量小于n，可以添加开括号
            if left_count < n:
                backtrack(s + "(", left_count+1, right_count)
            # 如果闭括号数量小于开括号数量，可以添加闭括号
            if right_count < left_count:
                backtrack(s + ")", left_count, right_count+1)
                
        backtrack()
        return ans         
# @lc code=end

