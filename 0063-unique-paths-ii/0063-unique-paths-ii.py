from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        @cache  # Memoization converts Backtracking -> DP!
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            
            return dfs(r + 1, c) + dfs(r, c + 1)

        return dfs(0, 0)