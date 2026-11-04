class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result= []
        path = []
        def is_pal(s,l,r):
            while l < r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(start):
            if start==len(s):
                result.append(path[:])
                return 
            for index in range(start,len(s)):
                if is_pal(s,start,index):
                    path.append(s[start:index+1])
                    dfs(index+1)
                    path.pop()

        dfs(0)
        return result