class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Left = 0
        Right = 1
        maxProfit = 0
        
        while Right < len(prices):
            if prices[Left] > prices[Right]:
                Left = Right
            
            curProfit = prices[Right] - prices[Left]
            if curProfit > maxProfit:
                maxProfit = curProfit
    
            Right += 1
        
        return maxProfit
        