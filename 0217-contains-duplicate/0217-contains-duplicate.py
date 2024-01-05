class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #return sorted(set(nums)) != sorted(nums)
    
        seen = {}
        length = len(nums)
        
        for i in range(length):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        
        return False