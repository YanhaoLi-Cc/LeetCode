#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
# from collections import defaultdict
# import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Solution 1
        # # 1. 构建图的邻接表
        # dct = defaultdict(dict)
        # for a, b, p in flights:
        #     dct[a][b] = p  # a -> b 的航班价格为 p

        # # 2. 初始化
        # visit = [n+1] * n  # visit数组记录到达每个城市的最小中转次数，初始为一个不可能的高值
        # stack = [[0, src, 0]]  # 优先队列，存储格式为 [累计成本, 当前城市, 已使用中转次数]
        # heapq.heapify(stack)

        # # 3. Dijkstra 算法的变体
        # while stack:
        #     cost, pos, cnt = heapq.heappop(stack)  # 取出当前累计成本最低的路径
        #     if pos == dst:
        #         return cost  # 到达目标城市 dst，返回成本
        #     if cnt >= visit[pos] or cnt > k:
        #         continue  # 如果已使用的中转次数多于 k 或存在更优路径，跳过
        #     visit[pos] = cnt  # 更新 visit 数组中的中转次数
        #     for nex in dct[pos]:  # 扩展到邻接的城市
        #         heapq.heappush(stack, [cost + dct[pos][nex], nex, cnt + 1])  # 将新路径加入堆中
        # return -1  # 未找到符合条件的路径，返回 -1
        
        # Solution 2
        # f[t][i] = cost 表示通过恰好 t 次航班，从出发城市 src 到达城市 i 需要的最小花费
        f = [[1e6] * n for _ in range(k + 2)]
        f[0][src] = 0  # 起点成本设为0

        # 动态规划状态转移
        for t in range(1, k + 2):  # 最多允许k+1次飞行
            for x, y, cost in flights:
                f[t][y] = min(f[t][y], f[t - 1][x] + cost)  # 更新到达y的最小成本

        # 计算结果，选择经过1到k+1次航班到达dst的最小成本
        ans = min([f[t][dst] for t in range(1, k + 2)])
        return -1 if ans == 1e6 else ans

# @lc code=end

# sol = Solution()

# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# n = 4
# src = 0
# dst = 3
# k = 1

# sol.findCheapestPrice(n, flights, src, dst, k)



