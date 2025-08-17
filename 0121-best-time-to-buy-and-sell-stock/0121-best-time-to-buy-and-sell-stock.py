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
                total = max(total, price - cur)
            else:
                cur = price

        return total
