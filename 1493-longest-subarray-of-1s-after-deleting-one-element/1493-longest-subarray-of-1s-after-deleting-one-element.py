class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        start = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero + 1
                zero = i
            
            length = max(length, i - start)
        
        return length