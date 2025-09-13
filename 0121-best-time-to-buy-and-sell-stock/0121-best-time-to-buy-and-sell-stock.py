class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = prices[0]
        max_price = 0

        for price in prices:
            if cur < price:
                max_price = max(max_price, price - cur)
            else:
                cur = price
        
        return max_price