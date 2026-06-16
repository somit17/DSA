class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,h=0,0
        curr_sum = 0
        result = float('inf')
        while(h < n):
            curr_sum+=nums[h]
            while(curr_sum >= target):
                result = min(result,h-l+1)
                curr_sum-=nums[l]
                l+=1
            h+=1
        return 0 if result == float('inf') else result
