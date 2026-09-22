class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(num):
            for i in range(1, len(num)):
                if i == 1:
                    num[i] = max(num[i], num[0])
                else:
                    num[i] = max(num[i-2] + num[i], num[i-1])

            return num[-1]
        
        return max(helper(nums[1:]), helper(nums[:-1]))
