class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        