class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)-1
        
        while L <= R:
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            
            M = (L + R)/2
            
            if nums[M] < target:
                L += 1
            else:
                R -= 1
        
        return -1
        