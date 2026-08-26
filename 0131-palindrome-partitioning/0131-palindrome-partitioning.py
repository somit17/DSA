class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.backtrack(s,0,[])
        return self.result


    def backtrack(self,s,start,current):

        if start == len(s):
            self.result.append(current[:])

        for end in range(start,len(s)):
            if self.is_palindrome(s,start,end):
                current.append(s[start:end+1])
                self.backtrack(s,end+1,current)
                current.pop()
        
    def is_palindrome(self,s,start,end):
        while start < end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True