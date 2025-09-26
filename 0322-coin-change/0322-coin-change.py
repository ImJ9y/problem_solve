class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp with 0 ~ amount + 1 list
        #try to find remain each amount index - coin(s)
        # if remain is >= 0 then we are going to find dp to calculate
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                remain = i - coin

                if remain >= 0:
                    dp[i] =  min(dp[i], 1 + dp[remain])

        return dp[amount] if dp[amount] != amount + 1 else -1