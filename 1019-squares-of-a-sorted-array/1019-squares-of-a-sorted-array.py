class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        L, R = 0, len(nums)-1

        while L <= R:
            if nums[L] * nums[L] < nums[R] * nums[R]:
                ans.append(nums[R] * nums[R])
                R -= 1
            else:
                ans.append(nums[L] * nums[L])
                L += 1
        
        return ans[::-1]
