class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_Num = max(nums)
        curr_Num = 0
        
        for i in range(len(nums)):
            if curr_Num < 0:
                curr_Num = 0
            
            curr_Num += nums[i]
            max_Num = max(max_Num, curr_Num)
        
        
        return max_Num