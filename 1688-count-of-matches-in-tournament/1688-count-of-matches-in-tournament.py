class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            temp = math.floor(n / 2)
            if n % 2 == 0:
                result += temp
            else:
                result += temp + 1
            n = math.floor(n / 2)
        return result