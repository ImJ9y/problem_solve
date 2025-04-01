class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_num = nums[0]

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest_num):
                closest_num = nums[i]
            elif abs(nums[i]) == abs(closest_num):
                if nums[i] > closest_num:
                    closest_num = nums[i]
        
        return closest_num