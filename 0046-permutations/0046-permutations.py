class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return 
            # if index == len(nums):
            #     return 
            for index in range(len(nums)):
                if used[index]: 
                    continue   
                #Take 
                used[index] = True
                path.append(nums[index])
                dfs()
                #Skip
                path.pop()
                used[index] = False
        
        dfs()
        return result