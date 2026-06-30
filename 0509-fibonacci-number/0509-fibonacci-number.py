class Solution:
    def fib(self, n: int) -> int:
        def _fib(n,memo):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            memo[n] = _fib(n-1,memo)+_fib(n-2,memo)
            return memo[n]
        return _fib(n,{})

        
        