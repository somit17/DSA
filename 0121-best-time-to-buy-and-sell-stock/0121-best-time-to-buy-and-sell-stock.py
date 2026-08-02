class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # for buy in range(0,len(prices)):
        #     for sell in range(buy + 1,len(prices)):
        #         profit = prices[sell] - prices[buy]
        #         print(f'S -> {prices[sell]} --- > B -> {prices[buy]}')
        #         max_profit = max(profit,max_profit)

        min_price = float('inf')
        for price in prices:
            min_price = min(price,min_price)
            max_profit = max(max_profit,price-min_price)
        return max_profit