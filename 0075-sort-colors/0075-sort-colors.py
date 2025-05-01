class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ans = [0,0,0]

        for num in nums:
            ans[num] += 1
        
        RED = ans[0]
        WHITE = ans[1]
        BLUE = ans[2]

        nums[:RED] = [0] * RED
        nums[RED:RED+WHITE] = [1] * WHITE
        nums[RED+WHITE:] = [2] * BLUE