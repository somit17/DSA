class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (2 * len(nums))
        #print(result)
        for i,num in enumerate(nums):
            #print(i)
            result[i] = num
            result[i+(len(nums))]=num
        return result
        