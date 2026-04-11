class Solution:
    def arrangeCoins(self, n: int) -> int:
        # res = 0
        # for i in range(1, n+1):
        #     if n < i:
        #         break
        #     n = n - i
        #     res = res+1
            
            
        # return res

        L,R = 1, n
        while L<=R:
            mid = (L+R)//2
            K = mid * (mid + 1) // 2
            if K > n:
                R = mid-1
            
            if K < n:
                L = mid + 1
            
            if K == n:
                return mid
        return R