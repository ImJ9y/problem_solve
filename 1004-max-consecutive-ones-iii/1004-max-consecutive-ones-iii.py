class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        max_length = 0
        num_zero = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[L] == 0:
                    num_zero -= 1
                L += 1
            
            max_length = max(max_length, R - L + 1)
        
        return max_length