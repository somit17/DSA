class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #We have to found boundaries
        start = self.lower_bound(nums,target)
        if start == len(nums) or nums[start]!=target:
            return [-1,-1]
        return [start,self.upper_bound(nums, target) - 1]
        
    def lower_bound(self,nums,target):
        l,r=0,len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


    def upper_bound(self,nums,target):
        l,r=0,len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l