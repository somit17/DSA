class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        result = []
        def backtrack(start,comb,current_sum):
            if current_sum == n and len(comb) == k:
                result.append(comb[:])
                return

            if current_sum > n:
                return 

            if len(comb) > k:
                return

            for idx in range(start,len(nums)):
                comb.append(nums[idx])
                backtrack(idx+1,comb,current_sum + nums[idx])
                comb.pop()
        backtrack(0,[],0)
        return result