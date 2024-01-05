class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = 0 
        R = 1
        max_profit = 0
        
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            cur_profit = prices[R] - prices[L]
            max_profit = max(max_profit, cur_profit)
            R += 1
        
        return max_profit