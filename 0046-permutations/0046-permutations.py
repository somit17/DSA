class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def dfs(index):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            if index == len(nums):
                return 
            if not used[index]:    
                #Take 
                used[index] = True
                path.append(nums[index])
                dfs(0)
                #Skip
                path.pop()
                used[index] = False
            dfs(index + 1) 
        
        dfs(0)
        return result