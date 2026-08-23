class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited=set()
        max_area = 0
        current_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    current_area = self.dfs(grid,row,col,visited)
                    max_area = max(max_area,current_area)
        return max_area

    def dfs(self,grid,r,c,visited):

        #Row and col bounds
        row_bounds = 0 <= r < len(grid)
        col_bounds = 0 <= c < len(grid[0])

        if not row_bounds or not col_bounds :
            return 0

        if grid[r][c] == 0:
            return 0

        pos = (r,c)
        if pos in visited:
            return 0
        
        visited.add(pos)
        count  = 1
        count+=self.dfs(grid,r+1,c,visited)
        count+=self.dfs(grid,r-1,c,visited)
        count+=self.dfs(grid,r,c+1,visited)
        count+=self.dfs(grid,r,c-1,visited)
        return count

        