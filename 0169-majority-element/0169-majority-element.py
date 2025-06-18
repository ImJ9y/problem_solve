class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most_num = {None:None}
        check = len(nums)//2

        for num in nums:
            if num in most_num:
                most_num[num] += 1
            else:
                most_num[num] = 1
        
        for key, value in most_num.items():
            if value > check:
                return key

        
        
        
