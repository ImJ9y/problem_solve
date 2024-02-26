class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums)
        for i in range(len(nums)):
            ans += (i - nums[i])
        
        return ans