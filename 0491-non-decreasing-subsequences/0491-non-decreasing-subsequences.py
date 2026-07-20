class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.result = set()
        self.current_subsequence = []
        self.backtrack(0)
        result = []
        for data in self.result:
            result.append(list(data))
        return result

    def backtrack(self,current_index):
        if len(self.current_subsequence)>=2:
            self.result.add(tuple(self.current_subsequence))
        
        #take and pop
        for next_index in range(current_index,self.n):
            if len(self.current_subsequence) == 0 or self.nums[next_index] >= self.current_subsequence[-1]:
                #Take 
                self.current_subsequence.append(self.nums[next_index])
                self.backtrack(next_index + 1)
                #Pop
                self.current_subsequence.pop()
            


        