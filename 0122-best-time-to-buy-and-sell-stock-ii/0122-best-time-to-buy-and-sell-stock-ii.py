class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = prices[0]
        max_profit = 0

        for price in prices:
            if cur < price:
                max_profit += price - cur
            
            cur = price
            
        return max_profit