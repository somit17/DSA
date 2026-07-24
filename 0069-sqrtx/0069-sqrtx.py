class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        l,r = 0,x
        while l <=r :
            mid = (l + r) // 2
            sq = mid * mid
            if  sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid -1
        return r