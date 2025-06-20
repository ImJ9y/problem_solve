class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {None:None}
        check = len(nums)//2

        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
            
        for key, val in ans.items():
            if val > check:
                return key
        