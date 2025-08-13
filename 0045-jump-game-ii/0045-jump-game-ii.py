class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, 0
        result = 0

        while R < len(nums)-1:
            farthest = 0
            for i in range(L, R+1):
                farthest = max(farthest, i + nums[i])
                print(farthest)
            
            L = R + 1
            R = farthest
            result += 1
        
        return result
        
