class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #maxNum = nums[0]
        maxNum = float('-inf') #default value
        curNum = 0
        
        for num in nums:
            curNum = max(curNum, 0) + num
            #or curNum += num
            maxNum = max(maxNum, curNum)
        
        return maxNum