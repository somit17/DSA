class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        #Base case
        if len(nums) == 0:
            return [ [] ]

        first = nums[0]
        full_perm = []
        for perm in self.permute(nums[1:]): #[[2,3] [3,2]]. # [[1,2,3] ,[2,1,3],[2,3,1]] [3,2]]
            for i in range(len(perm) + 1):
                full_perm.append(perm[:i] + [first] + perm[i:])
        
        return full_perm


        