class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # K = 1

        # while True:
        #     totaltime = 0
        #     for i in piles:
        #         totaltime += math.ceil(i/K)

        #     if totaltime <= h:
        #         return K
        #     K = K +1
        # return K         

        L, R = 1, max(piles)

        res = R
        while L<=R:
            mid = (L+R)//2
            total_time = 0
            for i in piles:
                total_time += math.ceil(i/mid)

            if total_time <= h:
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1
        return res 
            




