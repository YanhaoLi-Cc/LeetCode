#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from collections import Counter
from heapq import *

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         Solution 1
#         dic = Counter(nums)
        
#         heap = []
#         heapify(heap) # 将列表 heap 转换为一个堆
        
#         for key, value in dic.items():
#             if len(heap) < k:
#                 heappush(heap, (value, key))
#             else:
#                 if heap[0][0] < value:
#                     heappop(heap)
#                     heappush(heap, (value, key))
                
#         res = []
#         while heap:
#             top = heappop(heap)
#             res.append(top[1])

#         return res
        
        # Solution 2
        dic = Counter(nums)
        return [item[0] for item in dic.most_common(k)]

        
# @lc code=end

