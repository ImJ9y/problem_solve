class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            for i in range(1, len(nums)):
                if i == 1:
                    nums[i] = max(nums[i], nums[0])
                else:
                    nums[i] = max(nums[i] + nums[i-2], nums[i-1])
            
            return nums[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))