class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        def dfs(index,memo):
            if index in memo:
                return memo[index]
            if index >= len(cost):
                return 0
            #Take 1
            take1 = dfs(index + 1,memo)
            #Take 2
            take2 = dfs(index + 2,memo)
            memo[index] = cost[index] + min(take1,take2)
            return memo[index]
        memo = {}
        return min(dfs(0,memo),dfs(1,memo))
