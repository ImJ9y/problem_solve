class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        k = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k