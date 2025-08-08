class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = {}

        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        length = len(nums)//2

        for key, val in store.items():
            if val > length:
                return key
        
        