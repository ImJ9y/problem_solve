class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)

        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                remain = i - coin

                if remain < 0:
                    continue
                
                dp[i] = min(dp[i], 1 + dp[remain])
        
        return dp[amount] if dp[amount] != amount+1 else -1