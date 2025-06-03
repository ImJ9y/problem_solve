class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for num in nums:
            if abs(ans) > abs(num):
                ans = num
            elif abs(ans) == abs(num):
                if ans < num:
                    ans = num
        
        return ans