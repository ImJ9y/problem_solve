class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
        
        return False