class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_min, curr_max = 1, 1
        max_num = max(nums)
        
        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
            
            temp = curr_max * num
            curr_max = max(curr_min * num, curr_max * num, num)
            curr_min = min(curr_min * num, temp ,num)
            
            max_num = max(curr_max, max_num)
        
        return max_num