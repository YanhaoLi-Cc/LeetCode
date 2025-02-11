#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         phoneMap = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
        
#         combinations = []
#         combination = []
    
#         def backtrack(index):
#             if index == len(digits):
#                 combinations.append("".join(combination))
#             else:
#                 digit = digits[index]
#                 for item in phoneMap[digit]:
#                     combination.append(item)
#                     backtrack(index + 1)
#                     combination.pop()
        
#         if digits:
#             backtrack(0)
#         else:
#             return []
#         return combinations
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # 数字到字母的映射表
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        # 初始化列表作为队列，首先加入一个空字符串
        queue = [""]
        
        for digit in digits:
            letters = phoneMap[digit]
            # 对于列表中的每个已有组合，依次将新的字母附加进去
            for _ in range(len(queue)):
                # 从队列的头部取出一个组合
                current = queue.pop(0)
                # 将新字母添加到组合中，并将新的组合加入队列
                for letter in letters:
                    queue.append(current + letter)
        
        return queue


# @lc code=end

sol=Solution()
print(sol.letterCombinations("23"))