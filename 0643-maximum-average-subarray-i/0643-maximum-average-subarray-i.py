class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total+=nums[i]
        avg = total / k
        max_avg = avg
        for i in range(0,len(nums) - k):
            total-=nums[i]
            total+=nums[i+k]
            avg = total / k
            max_avg = max(max_avg,avg)
        return max_avg
        