class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0,0
        
        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2