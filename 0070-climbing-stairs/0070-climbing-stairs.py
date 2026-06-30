class Solution:
    def climbStairs(self, n: int) -> int:
        #using recursion
        # if n==2:
        #     return 2
        # if n==1:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        #Using memoisation
        def _climbStairs(n,memo):
            if n in memo:
                return memo[n]
            if n==2:
                return 2
            if n==1:
                return 1
            memo[n] = _climbStairs(n-1,memo) + _climbStairs(n-2,memo)
            return memo[n]
        return _climbStairs(n,{})
        
        