class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        return self.dfs(grid,0,0,{})

    def dfs(self,grid,r,c,memo):
        pos = (r,c)
        if pos in memo:
            return memo[pos]
        #Bounds
        r_b = 0 <= r < len(grid)
        c_b = 0 <= c < len(grid[0])
        if not r_b or not c_b:
            return float('inf')
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return grid[r][c]
        memo[pos] = grid[r][c] + min(self.dfs(grid,r+1,c,memo),self.dfs(grid,r,c+1,memo))
        return memo[pos]
        
