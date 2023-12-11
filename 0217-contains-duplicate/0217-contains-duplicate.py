class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #set() - used to convert an iterable to a sequence with unique elements
        #will distinct
        return len(set(nums)) != len(nums)
        