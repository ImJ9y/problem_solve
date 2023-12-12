class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #HashMap - O(n)
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in seen:
                #find list value's index (Values()), index
                return seen[diff], i
            else:
                #list value : index
                seen[nums[i]] = i
        
        return seen.values()
    
        # #O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j
                