#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
# from collections import Counter

# class Solution:
#     def topKFrequent(self, words: list[str], k: int) -> list[str]:
#         hash = Counter(words)
#         ans = sorted(hash, key=lambda word:(-hash[word], word))
        
#         return ans[:k]

import heapq
from collections import Counter

class Word:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        if self.value != other.value:
            return self.value < other.value  # 频率低的优先弹出
        return self.key > other.key         # 字母顺序大的优先弹出

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # 统计每个单词的出现次数
        cnt = Counter(words)
        # 定义小顶堆
        hp = []
        for key, value in cnt.items():
            heapq.heappush(hp, Word(key, value))
            # 维持堆的大小为 k
            if len(hp) > k:
                heapq.heappop(hp)
        # 对堆中的元素进行排序
        hp.sort(reverse=True)
        return [x.key for x in hp]

# @lc code=end
sol = Solution()

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
sol.topKFrequent(words=words, k=k)
