class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close_num = nums[0]

        for num in nums:
            if abs(close_num) > abs(num):
                close_num = num
            elif abs(close_num) == abs(num):
                if close_num < num:
                    close_num = num
        
        return close_num