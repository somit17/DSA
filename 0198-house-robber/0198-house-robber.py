class Solution:
    def rob(self, nums: List[int]) -> int:
        # def helper(i):
        #     if i < 0:
        #         return 0
        #     if i==0:
        #         return nums[0]
        #     rob = nums[i]+helper(i-2)
        #     skip = helper(i-1)
        #     return max(rob,skip)
        # return helper(len(nums)-1)

        def _rob(i,memo):
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            if i==0:
                return nums[0]
            
            take = nums[i]+_rob(i-2,memo)
            skip = _rob(i-1,memo)
            memo[i]= max(take,skip)
            return memo[i]
        return _rob(len(nums)-1,{})