class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def backtrack(i,j):
            if i < 0 or j < 0 or i>=m or j>=n or grid[i][j]=='$':
                return 0
            if grid[i][j]==0:
                return 0
            
            temp = grid[i][j]
            grid[i][j] = '$'
            max_gold = 0
            for dx,dy in directions:
                max_gold = max(max_gold,backtrack(dx+i,dy+j))
            grid[i][j] = temp
            return temp + max_gold
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    result = max(result, backtrack(i, j))
        return result