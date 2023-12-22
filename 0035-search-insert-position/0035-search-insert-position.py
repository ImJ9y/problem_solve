class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Left = 0
        Right = len(nums)-1
        
        while Left <= Right:
            Mid = (Left + Right) // 2

            if nums[Mid] < target:
                Left = Mid + 1
            elif nums[Mid] > target:
                Right = Mid - 1
            else:
                return Mid
        
        return Right + 1