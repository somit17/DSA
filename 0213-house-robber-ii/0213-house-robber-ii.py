class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_house(house_list):
            memo = {}
            def dfs(index,memo):
                if index in memo:
                    return memo[index]

                if index >= len(house_list):
                    return 0

                #Take 
                take = house_list[index] + dfs(index+2,memo)
                #skip
                skip = dfs(index+1,memo)
                memo[index] = max(take,skip)
                return memo[index]
            return dfs(0,memo)
        #A circle means house 0 and house n-1 can't both be robbed.
        #   Option A: rob houses 0..n-2  (ignore the last house)
        #   Option B: rob houses 1..n-1  (ignore the first house)
        
        return max(rob_house(nums[:-1]),rob_house(nums[1:]))