class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def dfs(index,memo):
            if index in memo:
                return memo[index]

            if index >= len(nums):
                return 0

            #Take 
            take = nums[index] + dfs(index+2,memo)
            #skip
            skip = dfs(index+1,memo)
            memo[index] = max(take,skip)
            return memo[index]
        return dfs(0,{})