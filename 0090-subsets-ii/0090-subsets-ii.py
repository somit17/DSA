class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        def backtrack(index,path):
            if len(nums) == index:
                result.append(path[:])
                return 
            #Take 
            path.append(nums[index])
            backtrack(index+1,path)
            #Skip
            path.pop()
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index+=1
            backtrack(index+1,path)
        backtrack(0,[])
        return result
        