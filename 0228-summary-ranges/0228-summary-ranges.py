class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(nums):
            start = i
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
            
            if nums[start] < nums[i]:
                ans.append(str(nums[start]) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[start]))
            
            i += 1
        
        return ans

