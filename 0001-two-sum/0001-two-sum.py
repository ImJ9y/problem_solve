class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}

        for i in range(len(nums)):
            cur = target - nums[i]
            if cur in result:
                return result[cur], i
            else:
                result[nums[i]] = i
        