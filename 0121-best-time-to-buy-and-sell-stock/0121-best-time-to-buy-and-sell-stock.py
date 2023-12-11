class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
    
#         profit = 0
        
#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 if prices[i] < prices[j]:
#                     if prices[j] - prices[i] < profit:
#                         continue
#                     else:
#                         profit = prices[j] - prices[i]

#         return profit
            
        