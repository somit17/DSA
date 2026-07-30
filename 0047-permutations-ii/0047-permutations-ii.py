class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        used = [False] * n
        def backtrack(perm):
            if len(perm)==n:
                if perm not in result:
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
        print(result)
        return result
        