class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #O(n) - Kadane’s Algorithm
        maxSum = nums[0]
#       maxNum = float('-inf') #default value
        curSum = 0
        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        
        return maxSum