class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sq_digits(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num = num // 10
            return total
        hash_set = set()
        while n > 1:
            if n in hash_set:
                return False
            hash_set.add(n)
            n = get_sq_digits(n)
        return True