class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0
        max_profit = 0
        for R in range(L+1 , len(prices)):
            if prices[R] < prices[L]:
                L = R
            else: 
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
        return max_profit




        # # Brute Force - 
        # max_profit = 0
        # for L in range(len(prices)):
        #     for R in range(L+1 , len(prices)):
        #         profit  = prices[R] - prices[L]
        #         max_profit = max(max_profit, profit)
        # return max_profit


