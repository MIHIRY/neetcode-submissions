class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0, num):

            if num == 1:
                return True

            if i*i == num:
                return True
            elif i*i > num:
                break
        return False
