class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins,amount,memo):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0

            min_coins = float('inf')
            for coin in coins:
                curr = 1 + helper(coins,amount - coin,memo)
                min_coins = min(curr,min_coins)
            memo[amount] = min_coins
            return memo[amount]
        ans =  helper(coins,amount,{})
        if ans == float('inf'):
            return -1
        else:
            return ans
        