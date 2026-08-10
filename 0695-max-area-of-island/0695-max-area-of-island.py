class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = float('-inf')
        size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.explore(grid,r,c,visited)
                max_area = max(max_area,size)

        return max_area
        
    def explore(self,grid,r,c,visited):

        row_bounds = 0 <= r < len(grid)
        col_bounds = 0 <= c < len(grid[0])

        if not row_bounds or not col_bounds:
            return 0
        
        if grid[r][c] == 0:
            return 0

        pos = (r,c)

        if pos in visited:
            return 0

        visited.add(pos)
        count = 1
        count+=self.explore(grid,r + 1,c,visited)
        count+=self.explore(grid,r - 1,c,visited)
        count+=self.explore(grid,r,c + 1,visited)
        count+=self.explore(grid,r,c - 1,visited)
        
        return count