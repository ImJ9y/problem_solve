class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for coin in coins:
            for i in range(amount+1):
                remainder = i - coin
                if remainder >= 0:
                    dp[i] = min(dp[i], dp[remainder] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1