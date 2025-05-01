class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1
        count = 1
        i = 0
        while i < len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                count += 1
            else:
                count = 1
            
            if i < len(nums)-1 and count < 3:
                nums[k] = nums[i+1]
                k += 1

            i += 1
            
        
        return k