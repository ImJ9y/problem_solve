class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        i = 0
        start = 0
        ans = []
        while start < len(nums): 
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1

            if nums[start] != nums[i]:
                ans.append(str(nums[start]) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[start]))
            
            start = i + 1
            i += 1
            
            
        return ans