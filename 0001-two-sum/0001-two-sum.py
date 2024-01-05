class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        length = len(nums)

        for i in range(length):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
            