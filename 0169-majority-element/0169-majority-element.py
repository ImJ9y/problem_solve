class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_array = {}

        for num in nums:
            if num in num_array:
                num_array[num] += 1
            else:
                num_array[num] = 1

        length = len(nums)/2

        for key, val in num_array.items():
            if val > length:
                return key
        