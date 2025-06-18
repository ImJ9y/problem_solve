class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cur = prices[0]
        for price in prices:
            if cur < price:
                profit += price-cur

            cur = price
        
        return profit