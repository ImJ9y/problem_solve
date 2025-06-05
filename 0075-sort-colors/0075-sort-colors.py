class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # res = [0,0,0]

        # for num in nums:
        #     res[num] += 1
        
        # RED = res[0]
        # WHITE = res[1]
        # BLUE = res[2]

        # nums[:RED] = [0] * RED
        # nums[RED:RED+WHITE] = [1] * WHITE
        # nums[WHITE+RED:] = [2] * BLUE

        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
