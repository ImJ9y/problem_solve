class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        L = 0
        R = 1
        
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            
            curr_profit = prices[R] - prices[L]
            max_profit = max(max_profit, curr_profit)
            R += 1
        
        return max_profit