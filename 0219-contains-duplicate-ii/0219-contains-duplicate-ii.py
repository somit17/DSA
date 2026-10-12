class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #1,2,3,1,2,3 k =2
        seen = set() #seen size always k
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
            
        