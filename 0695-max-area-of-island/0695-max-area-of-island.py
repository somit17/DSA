class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col)not in visited:
                    area = self.dfs(grid,row,col,visited)
                    max_area = max(max_area,area)

        return max_area
    def dfs(self,grid,r,c,visited):
        #Row and Col bounds
        rowBound = 0 <= r < len(grid)
        colBound = 0 <= c < len(grid[0])

        if not rowBound or not colBound:
            return 0
            
        if grid[r][c] == 0:
            return 0

        pos = (r,c)
        if pos in visited:
            return 0

        visited.add(pos)
        area = 1
        #Directions
        for dr,dc in self.directions:
            area += self.dfs(grid, r + dr, c + dc, visited)

        return area 