class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def _uniquePathsWithObstacles(obstacleGrid,r,c,memo):
            pos = (r,c)
            if pos in memo:
                return memo[pos]
            #Base Case
            if r == len(obstacleGrid) or c == len(obstacleGrid[0]) or obstacleGrid[r][c] == 1 :
                return 0 
            if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                return 1
            
            down = _uniquePathsWithObstacles(obstacleGrid,r+1,c,memo)
            right = _uniquePathsWithObstacles(obstacleGrid,r,c+1,memo)
            memo[pos] = down + right
            return memo[pos]
        return _uniquePathsWithObstacles(obstacleGrid,0,0,{})