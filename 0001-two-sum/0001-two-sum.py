class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if i == j:
                    continue
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]

        