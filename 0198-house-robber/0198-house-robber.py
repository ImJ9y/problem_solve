class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums)+1)

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-2])
        
        return dp[len(nums)-1]

        # rob1, rob2 = 0, 0

        # for num in nums:
        #     temp = max(num + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2