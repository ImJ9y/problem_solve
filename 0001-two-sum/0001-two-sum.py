class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in num_map:
                return [num_map[curr], i]
            else:
                num_map[nums[i]] = i
        
            
