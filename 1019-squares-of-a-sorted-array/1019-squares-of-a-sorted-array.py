class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        L, R = 0, len(nums)-1

        while L <= R:
            if nums[L] * nums[L] < nums[R] *nums[R]:
                res.append(nums[R] * nums[R])
                R -= 1
            else:
                res.append(nums[L] * nums[L])
                L += 1
        
        return res[::-1]