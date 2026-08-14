class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_prod = 0
        L = 0

        while L < len(nums):
            cur = 1
            for R in range(L, len(nums)):
                cur *= nums[R]
                if max_prod < cur:
                    max_prod = cur
            L += 1
        
        return max_prod
