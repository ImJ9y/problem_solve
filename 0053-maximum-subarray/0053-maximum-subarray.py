class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = max(nums)
        
        for num in nums: 
            curr_sum += num
            
            if curr_sum < 0:
                curr_sum = 0
                continue
            else:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
            