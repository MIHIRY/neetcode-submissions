class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # L,R = 0, len(heights)-1
        # hold = 0
        # while L < R:
        #     res = min(heights[L], heights[R])* (R-L)

        #     hold = max(res, hold)
        #     if heights[L] < heights[R]:
        #         L = L + 1
        #     else:
        #         R = R -  1
        # return hold

        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r-l) * min(heights[l],heights[r])
                res = max(res,area)
        return res