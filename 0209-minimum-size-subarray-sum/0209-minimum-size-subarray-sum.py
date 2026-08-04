class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_len = float('inf')
        curr_sum = 0
        for end in range(len(nums)):
            curr_sum+=nums[end]
            while curr_sum >= target:
                #print(f'INSIDE WHILE')
                min_len = min(min_len,end - start + 1)
                curr_sum-=nums[start]
                #print(f'CURR-> {curr_sum}')
                #print(f'START-> {start}')
                start+=1
            #print(f'CURRENT - {curr_sum}')
            #if curr_sum == target:
                #print(f'INSIDE')
                #min_len = min(min_len,end - start + 1)
            
        return 0 if min_len == float('inf') else min_len