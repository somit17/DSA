class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.result = []
        
        self.backtrack(1,[])
        
        return self.result 
        
    def backtrack(self,index,combo):
        if len(combo) == self.k:
            self.result.append(combo[:])
            return 
        for num in range(index,self.n + 1):
            combo.append(num)
            self.backtrack(num+1,combo)
            combo.pop()