class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {None:None}

        for i in range(len(nums)):
            if nums[i] in result:
                result[nums[i]] += 1
            else:
                result[nums[i]] = 1
        
        max_num = 0
        ans = 0
        for key, val in result.items():
            if max_num < val:
                max_num = val
                ans = key

        return ans