class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, len(nums)-1
        ans = []

        while L <= R:
            if nums[L] < nums[R]:
                ans = min(ans, nums[L])
                break
            
            M = (L+R)//2

            ans = min(ans, nums[M])
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M - 1
        
        return ans