class Solution:
    def fib(self, n: int) -> int:
        return self._fib(n,{})
    def _fib(self,n,memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = self._fib(n-1,memo) + self._fib(n-2,memo)
        return memo[n]