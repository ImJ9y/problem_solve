class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k