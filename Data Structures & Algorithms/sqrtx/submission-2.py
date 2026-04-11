class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x

        while L <=R:
            mid = (L+R)//2
            if mid*mid > x:
                R = mid -1
            elif mid*mid < x:
    
                L = mid+1
            elif mid*mid == x:
                return mid
        return R


        