class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    if (row,col) not in visited:
                        self.dfs(grid,row,col,visited)
                        count+=1
        return count
    def dfs(self,grid,r,c,visited):
        row_bound = 0 <= r < len(grid)
        col_bound = 0 <= c < len(grid[0])
        if not row_bound or not col_bound:
            return 
        
        if grid[r][c] == '0':
            return 
        
        pos = (r,c)
        if pos in visited:
            return 
        
        visited.add(pos)
        
        for dr,dc in self.directions:
            nr = dr + r
            nc = dc + c
            self.dfs(grid,nr,nc,visited)
                
