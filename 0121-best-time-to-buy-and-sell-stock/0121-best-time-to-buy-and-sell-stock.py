class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_price = prices[0]
        max_price = 0
        
        for price in prices:
            if price < cur_price:
                cur_price = price
            else:
                max_price = max(max_price, price - cur_price)
        
        return max_price