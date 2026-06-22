class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #print(n)
        expected_total = n * (n + 1) / 2
        #print(total)
        current_total = sum(nums)
        print(current_total)
        return math.floor(expected_total - current_total)