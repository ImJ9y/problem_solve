class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums)-1
        
        if nums[0] == target:
            return 0
        
        while L < R:
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            
            M = (L+R)/2
            
            if nums[M] > target:
                L += 1
            elif nums[M] < target:
                R -= 1
            elif nums[M] == target:
                return M
            
        return -1