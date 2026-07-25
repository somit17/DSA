class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        def get_sq_digits(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n = n //10
            return total
        while n > 1:
            if n in hash_set:
                return False
            hash_set.add(n)
            n = get_sq_digits(n)
        
        return True