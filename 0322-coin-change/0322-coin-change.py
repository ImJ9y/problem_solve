class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
    
        for i in range(amount + 1):
            for coin in coins:
                remain = i - coin
                if remain >= 0:
                    dp[i] = min(dp[i], 1 + dp[remain])
        
        return dp[amount] if dp[amount] != amount + 1 else -1 #larger than any possible number of coins needed