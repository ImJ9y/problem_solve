class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_pivot = [0] * len(nums)
        right_pivot = [0] * len(nums)

        for i in range(1, len(nums)):
            left_pivot[i] = left_pivot[i-1] + nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_pivot[i] = right_pivot[i+1] + nums[i+1]

        for i in range(len(nums)):
            if left_pivot[i] == right_pivot[i]:
                return i
        
        return -1
