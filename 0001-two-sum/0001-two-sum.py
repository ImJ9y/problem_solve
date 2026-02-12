class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            cur = target-nums[i]
            if cur in num_map:
                return i, num_map[cur]
            else:
                num_map[nums[i]] = i
