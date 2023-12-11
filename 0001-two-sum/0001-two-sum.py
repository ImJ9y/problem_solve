class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                sum = nums[i] + nums[j]
                if i == j:
                    continue
                
                if sum == target:
                    return i,j