class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        window_sum = 0
        min_size = float('inf')

        for end in range(len(nums)):
            window_sum+=nums[end]

            while window_sum >= target:
                min_size = min(min_size,end - start + 1)
                window_sum-= nums[start]
                start+=1
            
        return 0 if min_size == float('inf') else min_size