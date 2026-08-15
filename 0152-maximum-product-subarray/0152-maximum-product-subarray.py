class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        min_num = 0
        max_num = 0
        max_product = 0

        for num in nums:
            temp = max_num
            max_num = max(num, num * max_num, num * min_num)
            min_num = min(num, num * min_num, num * temp)

            max_product = max(max_product, max_num)
        
        return max_product