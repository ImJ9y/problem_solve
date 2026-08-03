class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1): #front
            for j in range(i+1, len(nums)): #back
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)