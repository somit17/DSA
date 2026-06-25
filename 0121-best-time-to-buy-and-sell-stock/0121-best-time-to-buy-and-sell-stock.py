class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0
        for end in range(1,len(prices)):
            curr_profit = prices[end] - prices[start]
            
            print(f'Current - {curr_profit}')
            while start < end and prices[start] > prices[end]:
                print(f'INSIDE - ')
                print(f'START - {start}')
                start+=1
                curr_profit = prices[end] - prices[start]
                print(f'curr_profit - {curr_profit}')
            #print(f'Current - {curr_profit}')
            max_profit = max(max_profit,curr_profit)
            print(f'Max - {max_profit}')
        return max_profit 
        #print(max_profit)