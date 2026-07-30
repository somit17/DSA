class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                perm.append(nums[i])
                used[i] = True
                backtrack(perm)
                perm.pop()
                used[i] = False
        backtrack([])
        print(result)
        return result
        