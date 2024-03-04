class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = [1] * len(nums)
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        R = nums[-1]
        
        for j in range(len(nums)-2,-1,-1):
            ans[j] = ans[j] * R
            R = nums[j] * R
        
        return ans
            