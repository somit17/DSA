class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = self.reverseNum(n)
        return abs( n - rev)

    def reverseNum(self,n):

        reversed_num = 0

        while n > 0:
            digit = n % 10
            reversed_num = reversed_num * 10 + digit
            n = n // 10
        print(reversed_num)
        return reversed_num
        