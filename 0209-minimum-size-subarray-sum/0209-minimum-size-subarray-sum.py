class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        cur_sum = 0
        min_len = float('inf')

        for R in range(len(nums)):
            cur_sum += nums[R]

            while cur_sum >= target:
                min_len = min(min_len, R - L + 1)
                cur_sum -= nums[L]
                L += 1


        return min_len if min_len < float('inf') else 0
