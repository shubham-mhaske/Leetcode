# Last updated: 8/21/2025, 3:00:09 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        if N<=1:
            return max_profit
        L,R = 0,1
        while R<N:
            profit = prices[R] - prices[L]
            if profit<=0:
                L=R    
            elif profit>max_profit:
                max_profit = profit
            R+=1
        return max_profit
        
        