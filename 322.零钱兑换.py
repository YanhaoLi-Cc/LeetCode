#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [1e6] * (amount + 1)
        dp[0] = 0


        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[amount] == 1e6:
            return -1
        else:
            return dp[amount]
# @lc code=end

