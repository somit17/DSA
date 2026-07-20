class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n
        def backtrack(per):
            if len(per)==n:
                result.append(per[:])
                return 
            for i in range(n):
                if used[i] == True:
                    continue
                used[i] = True
                per.append(nums[i])
                backtrack(per)
                per.pop()
                used[i] = False
                
        backtrack([])
        return result

        