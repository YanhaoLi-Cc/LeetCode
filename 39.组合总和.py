#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        backtrack(start, target, path)函数实现回溯过程
        start参数表示从候选数组的哪个位置开始考虑
        target参数表示当前还需要凑成的目标值
        path参数记录当前已选的数字组合
        '''
        
        results = []
        candidates.sort()
        
        def backtrack(start, target, path):
            if target == 0:
                results.append(path[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                backtrack(i, target-candidates[i], path+[candidates[i]])
        
        backtrack(0, target, [])
        return results
        
# @lc code=end

sol = Solution()
candidates = [2,3,5]
target = 7
sol.combinationSum(candidates, target)
