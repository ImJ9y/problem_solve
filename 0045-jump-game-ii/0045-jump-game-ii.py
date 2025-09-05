class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, 0
        cur = 0
        result = 0

        while R < len(nums)-1:
            for i in range(L, R+1):
                cur = max(cur, i + nums[i])
            
            L = R + 1
            R = cur
            result += 1
        
        return result
