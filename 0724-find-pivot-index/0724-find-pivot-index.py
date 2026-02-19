class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        # total_sum = left_sum + nums[i] + right_sum
        for i, x in enumerate(nums):
            if left_sum == total_sum - left_sum - x:
                return i
            
            left_sum += x

        return -1
