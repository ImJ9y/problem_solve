class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = {None:None}
        n = len(nums)/2

        for num in nums:
            if num in num_list:
                num_list[num] += 1
            else:
                num_list[num] = 1

        for key, count in num_list.items():
            if count > n:
                return key
        
