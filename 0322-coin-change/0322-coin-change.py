class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        ans = self._coinChange(coins,amount,{})
        return -1 if ans == float('inf') else ans
    def _coinChange(self,coins,amount,memo):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        min_coin = float('inf')
        for coin in coins:
            curr_coin = 1 + self._coinChange(coins,amount - coin,memo)
            min_coin = min(min_coin,curr_coin)
            memo[amount] = min_coin
        return memo[amount]

#               [11]
#   [1]         [2]         [5]
#   [1][2][5]   [1][2][5]   [1][2][5]
#                                    [1] ==11   [5,5,1]
        