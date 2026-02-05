class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zero = 0
        count = 0
        L = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                num_zero += 1

            while num_zero > k:
                if nums[L] == 0:
                    num_zero -= 1
                L += 1
            
            count = max(count, R - L + 1)
            
        return count