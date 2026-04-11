class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for i in range(0, num):

        #     if num == 1:
        #         return True

        #     if i*i == num:
        #         return True
        #     elif i*i > num:
        #         break
        # return False

        L,R = 1, num 
        while L<= R:
            mid = (L+R)//2
            sqrt = mid*mid
            if sqrt > num:
                R = mid - 1
            elif sqrt < num:
                L = mid + 1

            else:    
                return True
        return False 