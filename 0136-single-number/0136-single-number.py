class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.append(num)
        
        return seen[0]