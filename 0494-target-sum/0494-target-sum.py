class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        def dfs(index,current,memo):
            if index == len(nums):
                return 1 if current==target else 0
            state = (index,current)
            if state in memo:
                return memo[state]
            #Choice 1 +
            plus = dfs(index + 1,current + nums[index],memo) 
            #Choice 2 -
            minus = dfs(index + 1,current - nums[index],memo)
            memo[state] =  plus + minus
            return memo[state]
        return dfs(0,0,memo)