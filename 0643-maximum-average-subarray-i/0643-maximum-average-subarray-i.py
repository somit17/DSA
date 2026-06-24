import numpy as np
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        #print(f'CURRENT - {current_sum}')
        current_avg = current_sum / k
        max_avg = current_avg
        #print(result)
        for i in range(0,len(nums)- k):
            current_sum-=nums[i]
            #print(f'REMOVED = {nums[i]}')
            current_sum+=nums[i+k]
            #print(f'ADDED = {nums[i+k]}')
            #print(f'AVG = {current_sum / k}')
            max_avg = max(max_avg,current_sum / k)
        return max_avg

        