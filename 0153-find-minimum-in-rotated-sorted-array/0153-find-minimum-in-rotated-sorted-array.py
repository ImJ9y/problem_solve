class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_num = float('inf')
        for i in range(len(nums)):
            cur = nums[i]
            if min_num > cur:
                min_num = min(min_num, cur)

        return min_num