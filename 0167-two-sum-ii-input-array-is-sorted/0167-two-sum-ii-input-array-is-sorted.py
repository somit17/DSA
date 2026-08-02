class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen  = {}
        for idx,num in enumerate(numbers):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment],idx+1]
            seen[num]= idx + 1
        