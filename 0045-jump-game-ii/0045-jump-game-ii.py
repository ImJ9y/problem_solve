class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, 0
        farthest = 0
        count = 0

        while R < len(nums)-1:
            for i in range(L, R+1):
                farthest = max(farthest, nums[i] + i)
            
            L = R+1
            R = farthest
            count += 1
        
        return count
