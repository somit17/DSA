class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliments = {}
        for idx,n in enumerate(numbers):
            other_num = target - n
            if other_num in compliments:
                return [compliments[other_num],idx+1]
            compliments[n] = idx+1