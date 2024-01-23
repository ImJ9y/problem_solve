class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_num = 0
        max_num = max(nums)
        
        for num in nums:
            if curr_num < 0:
                curr_num = 0
            
            curr_num += num
            max_num = max(curr_num, max_num)
        
        return max_num
            
        
        