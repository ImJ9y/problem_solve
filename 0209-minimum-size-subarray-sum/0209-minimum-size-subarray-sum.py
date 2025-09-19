class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        min_length = float('inf')
        cur_sum = 0


        for R in range(len(nums)):
            cur_sum += nums[R]

            while cur_sum >= target:
                min_length = min(min_length, R - L + 1)
                cur_sum -= nums[L]
                L += 1
        
        return min_length if min_length < float('inf') else 0