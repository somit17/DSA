class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.non_obs = 0
        self.result = 0
        self.x =0
        self.y = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    self.non_obs+=1
                elif grid[i][j] == 1:
                    self.non_obs+=1
                    self.x = i
                    self.y = j
        self.backtrack(grid,0,self.x,self.y)
        return self.result

    def backtrack(self,grid,count,x,y):
        if x < 0 or y < 0 or x >= self.m or y >= self.n or grid[x][y]==-1:
            return 
        if grid[x][y] == 2:
            if count == self.non_obs:
                self.result+=1
            return 

        grid[x][y]=-1

        for d in self.directions:
            self.backtrack(grid,count+1,x + d[0],y + d[1])

        grid[x][y]=0

        