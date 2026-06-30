class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def helper(r,c):
        #     #Base cases
        #     #Out of bound
        #     if r == m or c == n:
        #         return 0
        #     #Path found
        #     if r == m - 1 and c == n - 1:
        #         return 1
        #     down = helper(r+1,c)
        #     right = helper(r,c+1)
        #     return down+right
        # return helper(0,0)

        #Using memoisation
        def _uniquePaths(r,c,memo):
            #Base cases
            #if element found
            pos = (r,c)
            if pos in memo:
                return memo[pos]
            #Out of bound
            if r == m or c == n:
                return 0
            #Path found
            if r == m - 1 and c == n - 1:
                return 1
            down = _uniquePaths(r+1,c,memo)
            right = _uniquePaths(r,c+1,memo)
            memo[pos] = down+right
            return memo[pos]
        return _uniquePaths(0,0,{}) 