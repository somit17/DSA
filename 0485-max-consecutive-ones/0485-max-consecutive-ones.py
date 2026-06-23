class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_max = 0 
        for num in nums:
            if num==1:
                current_max+=1
                max_count = max(max_count,current_max)
            else:
                current_max = 0
        return max_count