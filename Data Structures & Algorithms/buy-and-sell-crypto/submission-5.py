class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx_l = 0
        idx_r = 1
        max_diff = 0
        while idx_r <len(prices):
            if (prices[idx_l] < prices[idx_r]):              
                profit = prices[idx_r] - prices[idx_l]
                max_diff = max(max_diff, profit)
            else:
                idx_l=idx_r
            idx_r += 1
        return max_diff
                
            


        