class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        cur = prices[0]
        for price in prices:
            if cur < price:
                total = max(total, price - cur)
            else:
                cur = price
        
        return total
            