class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return self.dfs(grid,row,col,visited)
        return 0


    def dfs(self,grid,r,c,visited):

        #Row and Col inbounds
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 1
            
        if grid[r][c] == 0:
            return 1

        pos = (r,c)
        if pos in visited:
            return 0

        visited.add(pos)

        perimeter = 0
        perimeter+=self.dfs(grid,r+1,c,visited)
        perimeter+=self.dfs(grid,r-1,c,visited)
        perimeter+=self.dfs(grid,r,c+1,visited)
        perimeter+=self.dfs(grid,r,c-1,visited)
        return perimeter