class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [1] * len(nums)

        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i +1 , len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        
        # return max(dp)

        output = []

        for num in nums:
            if len(output) == 0 or output[-1] < num:
                output.append(num)
            else:
                index = bisect_left(output, num)
                output[index] = num
            
        
        return len(output)