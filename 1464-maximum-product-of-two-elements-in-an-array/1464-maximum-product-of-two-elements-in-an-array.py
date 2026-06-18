class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        result = 0
        for i in range(1,len(nums)):
            result = max(result , (nums[i]-1) * (curr_max - 1))
            curr_max = max(nums[i],curr_max)
        return result