class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if num == 1:
        #     return True
        
        # for i in range(num):
        #     if i*i == num:
        #         return True
        #     if i*i > num:
        #         return False
        # return False
        
        if num == 1:
            return True
        
        L, R = 1, num

        while L <= R:
            mid = (L+R)//2

            if mid * mid > num:
                R = mid-1
            elif mid * mid < num:
                L = mid + 1
            else:
                return True
        return False 

