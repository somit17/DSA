class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if mid == num // mid and sq == num:
                return True
            elif mid > num // mid:
                r = mid - 1
            else:
                l = mid + 1
        return False
        