class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros_count = 0
        total = 0
        start = 0

        for end in range(len(nums)):
            if nums[end]==0:
                zeros_count+=1

            while zeros_count > k:
                if nums[start]==0:
                    zeros_count-=1
                start+=1

            total = max(total,end - start + 1)
        return total
        