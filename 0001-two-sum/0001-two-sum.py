class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for idx,num in enumerate(nums):
            remaining = target - num
            if remaining in compliments:
                return [idx,compliments[remaining]]
            compliments[num] = idx

        