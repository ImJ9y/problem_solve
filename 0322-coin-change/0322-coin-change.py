class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for coin in coins:
            for i in range(1, amount+1):
                remainder = i - coin
                if remainder >= 0:
                    dp[i] = min(dp[i], dp[remainder] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1


        #[0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        # coin = 1, 2, 5

        # amount = 1
        # coin = 1

        # [0, 1, 2, ]