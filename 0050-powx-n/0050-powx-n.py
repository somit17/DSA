class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If n is negative, compute positive power and invert
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        # Base cases
        if n == 0:
            return 1.0
        if n == 1:
            return x
        
        # Recursive step – fast exponentiation
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x