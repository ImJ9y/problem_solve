class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        cur = prices[0]
        for price in prices:
            if cur < price:
                max_profit = max(max_profit, price-cur)
            else:
                cur = price
        
        return max_profit
            
                