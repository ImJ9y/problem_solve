class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = 0
        R = 1
        max_price = 0
        
        while R < len(prices):
            if prices[L] > prices[R]:
                L += 1
                R = L
            else:
                curr_price = prices[R] - prices[L]
                max_price = max(curr_price, max_price)
            
            R += 1
            
        return max_price