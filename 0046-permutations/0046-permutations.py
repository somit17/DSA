class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        result = []
        def backtrack(perm):
            if len(perm) == n:
                result.append(perm[:])
                return 
            for i in range(n):
                if used[i]:
                    continue 
                perm.append(nums[i])
                used[i] = True
                backtrack(perm)
                perm.pop()
                used[i] = False

        backtrack([])
        return result
        