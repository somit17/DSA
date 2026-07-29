class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        count = 0
        visited=  [[False] * len(grid[0]) for _ in range(len(grid))]
        def explore(grid,r,c,visited):
            if r < 0 or c < 0 or r >= len(grid) or c >=len(grid[0]):
                return False
            if visited[r][c]:
                return False
            if grid[r][c]=='0':
                return False
            visited[r][c] = True
            for d in directions:
                explore(grid,d[0]+r,d[1]+c,visited)
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if explore(grid,i,j,visited):
                    count+=1
        return count
        