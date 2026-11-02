class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []
        def dfs(index,total):
            if total == target:
                result.append(path[:])
                return 
            if total > target or index == len(candidates):
                return 
            #Take 
            path.append(candidates[index])
            dfs(index,total + candidates[index])
            #Exclude
            path.pop()
            dfs(index + 1,total)

        dfs(0,0)
        return result