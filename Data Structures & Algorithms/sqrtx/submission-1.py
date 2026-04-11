class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        ans = 0
        while L <=R:
            mid = (L+R)//2
            if mid*mid > x:
                R = mid -1
            elif mid*mid < x:
                ans = mid
                L = mid+1
            elif mid*mid == x:
                return mid
        return R


        