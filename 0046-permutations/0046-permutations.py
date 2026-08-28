class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.used = set()
        self.explore(nums,[])
        return self.result
    
    def explore(self,nums,perm):
        if len(perm) == len(nums):
            self.result.append(perm[:])
            return 

        for i in range(0,len(nums)):
            num = nums[i]
            if num not in self.used:
                #Take 
                self.used.add(num)
                perm.append(num)
                #Explore
                self.explore(nums,perm)
                #Reject
                perm.pop()
                self.used.remove(num)