class Solution:
    def palindrome(self,s):
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.result =[]
        self.n = len(s)
        self.backtrack(0,[])
        return self.result
    def backtrack(self,index,current_partition):
        if index == self.n:
            self.result.append(current_partition[:])
            return
        #Try all possible solutions
        for end in range(index,self.n):
            substring = self.s[index:end+1]
            if self.palindrome(substring):
                current_partition.append(substring)
                self.backtrack(end+1,current_partition)
                current_partition.pop()

                

        