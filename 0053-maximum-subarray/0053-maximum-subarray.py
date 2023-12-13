class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
        
        return maxSum
        
        
        
        
        
        #maxNum = nums[0]
#         maxNum = float('-inf') #default value
#         curNum = 0
        
#         for num in nums:
#             curNum = max(curNum, 0) + num
#             #or curNum += num
#             maxNum = max(maxNum, curNum)
        
#         return maxNum