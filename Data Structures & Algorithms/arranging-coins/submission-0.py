class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if n < i:
                break
            n = n - i
            res = res+1
            
            
        return res