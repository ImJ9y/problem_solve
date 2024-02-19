class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        L = 0
        R = len(nums)-1
        
        while L <= R:
            if nums[L] < nums[R]:
                ans = min(ans, nums[L])
                break
            
            M = (L + R)/2
            
            ans = min(ans, nums[M])
            
            if nums[R] < nums[M]:
                L = M + 1
            else:
                R = M - 1
                
        return ans
            
            
            
        
    
                
            