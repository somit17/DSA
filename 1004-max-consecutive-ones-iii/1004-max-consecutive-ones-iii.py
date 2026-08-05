class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        start = 0
        zeros_count = 0 

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros_count+=1
            
            while zeros_count > k:
                if nums[start] ==0:
                   zeros_count-=1
                start+=1
            count = max(count,end - start + 1)
        return count 