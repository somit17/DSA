class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        l,r = 1,x
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
            
        return ans
        