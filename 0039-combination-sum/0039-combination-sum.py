class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index,comb,current_sum):
            if current_sum == target:
                result.append(comb[:])
                return
            if current_sum > target:
                return 
            for idx in range(index,len(candidates)):
                comb.append(candidates[idx])
                backtrack(idx,comb,candidates[idx]+current_sum)
                comb.pop()
        backtrack(0,[],0)
        return result