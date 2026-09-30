class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        self.length = len(nums)
        result = [0] * (2 * self.length)
        for idx in range(len(nums)):
            result[idx] = nums[idx]
            result[idx + self.length] = nums[idx] 
        print(result)
        return result
        