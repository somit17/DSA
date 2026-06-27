class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums:
        #     return nums
        # n = len(nums)
        # k = k % n
        # if k > 0:
        #     nums[:]=nums[-k:]+nums[:-k]

        #Using old approach
        def reverse(start:int,end:int) -> None:
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        n = len(nums)
        k = k % n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

