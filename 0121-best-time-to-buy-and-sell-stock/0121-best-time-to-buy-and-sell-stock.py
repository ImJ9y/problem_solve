class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Two Pointers
        Left = 0
        Right = 1
        maxProfit = 0
        while Right < len(prices):
            if prices[Left] < prices[Right]:
                profit = prices[Right] - prices[Left]
                maxProfit = max(maxProfit, profit)
            else:
                Left = Right
            Right += 1
        return maxProfit
        
        
#         while Right < len(prices):
#             if prices[Left] > prices[Right]:
#                 Left = Right
            
#             curProfit = prices[Right] - prices[Left]
#             if curProfit > maxProfit:
#                 maxProfit = curProfit
    
#             Right += 1
        
#         return maxProfit
        
        
        