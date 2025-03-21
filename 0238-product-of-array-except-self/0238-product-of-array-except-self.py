class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]

        R = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            ans[i] *= R
            R *= nums[i]
        
        return ans