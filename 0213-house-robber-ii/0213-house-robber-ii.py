class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def helper(nums):
            rob1, rob2 = 0,0
            
            for num in nums:
                temp = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        