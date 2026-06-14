class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for idx,num in enumerate(nums):
            other_num = target - num
            if other_num in compliments:
                return [idx,compliments[other_num]]
            compliments[num]=idx        