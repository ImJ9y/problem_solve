class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]

        R = nums[-1]

        for i in range(len(nums)-2, -1,-1):
            output[i] *= R
            R *= nums[i]
        
        return output