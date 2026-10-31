class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.non_obs = 0
        self.result = 0
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        x = 0
        y = 0

        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c]==0:
                    self.non_obs+=1
                if grid[r][c]==1:
                    self.non_obs+=1
                    x = r
                    y = c
        self.dfs(grid,x,y,0)
        return self.result

    def dfs(self,grid,r,c,count):
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
             return 
        if grid[r][c] == -1:
            return
        if grid[r][c] == 2:
            if count == self.non_obs:
                self.result+=1
            return 
        temp = grid[r][c] 
        grid[r][c]  = -1

        for dr,dc in self.directions:
            self.dfs(grid,r+dr,c+dc,count+1)

        grid[r][c]=temp
        