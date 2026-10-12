class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = sum(nums[:k])
        max_avg = curr / k
        for i in range(k,len(nums)):
            curr+=nums[i] - nums[i-k]
            max_avg = max(max_avg,curr / k)
        return max_avg