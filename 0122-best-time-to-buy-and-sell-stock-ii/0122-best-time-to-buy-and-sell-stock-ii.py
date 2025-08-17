class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = prices[0]
        total = 0

        for price in prices:
            if cur < price:
                total += price - cur
            
            cur = price
        
        return total
        