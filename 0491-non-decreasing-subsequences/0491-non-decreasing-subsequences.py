class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(nums,0,[])
        return self.result

    def backtrack(self,nums,idx,path):

        if len(path)>=2:
            self.result.append(path[:])

        used = set()
        for i in range(idx,len(nums)):
            if (path and nums[i] < path[-1]) or (nums[i] in used):
                continue
            
            used.add(nums[i])
            path.append(nums[i])
            self.backtrack(nums,i+1,path)
            path.pop()

