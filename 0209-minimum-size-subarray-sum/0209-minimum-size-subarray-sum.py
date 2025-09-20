class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        L = 0
        output = float('inf')
        cur = 0

        for R in range(len(nums)):
            cur += nums[R]
            while cur >= target:
                output = min(output, R - L + 1)
                cur -= nums[L]
                L += 1
        
        return output if output < float('inf') else 0
