class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_list = []

        for num in nums:
            squared_list.append(num*num)
        
        return sorted(squared_list)