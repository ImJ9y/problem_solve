class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        cur = 0
        min_len = float('inf')
        L = 0

        for R in range(len(nums)):
            cur += nums[R]

            while cur >= target:
                min_len = min(min_len, R - L + 1)
                cur -= nums[L]
                L += 1
            
        return min_len if min_len != float('inf') else 0