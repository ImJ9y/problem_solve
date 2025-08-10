class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current = prices[0]
        total = 0

        for price in prices:
            if current < price:
                total = max(price - current, total)
            else:
                current = price 
        
        return total
