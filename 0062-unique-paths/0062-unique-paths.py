class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        return self.dfs(0,0,{})
    def dfs(self,r,c,memo):
        pos = (r,c)
        if pos in memo:
            return memo[pos]
        #Bounds
        r_bounds = 0 <= r < self.m
        c_bounds = 0 <= c < self.n
        if not r_bounds or not c_bounds:
            return 0

        if r == self.m - 1 and c == self.n -1 :
            return 1
        memo[(pos)] = self.dfs(r,c+1,memo) + self.dfs(r + 1,c,memo)
        return memo[(pos)]