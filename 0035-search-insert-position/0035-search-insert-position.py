class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L + R)//2

            if nums[M] == target:
                return M
            elif nums[L] < target:
                L += 1
            elif nums[R] > target:
                R -= 1
        
        return L
            
        
        