class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        current = 0

        while current <= r:
            if nums[current]==0:
                nums[l],nums[current]=nums[current],nums[l]
                current+=1
                l+=1
            elif nums[current]==1:
                current+=1
            else:
                nums[r],nums[current]=nums[current],nums[r]
                r-=1