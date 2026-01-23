class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            first_step = dp[i-2] + cost[i-2]
            second_step = dp[i-1] + cost[i-1]

            dp[i] = min(first_step, second_step)

        return dp[-1]