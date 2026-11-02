class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result =[]
        path = []

        def dfs(index,total):
            if total == target:
                result.append(path[:])
                return 
            
            if total > target or index == len(candidates):
                return 

            #Take
            path.append(candidates[index])
            dfs(index + 1,total + candidates[index])
            #Skip       
            path.pop()
            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index+=1
            dfs(index + 1,total)
        dfs(0,0)
        return result