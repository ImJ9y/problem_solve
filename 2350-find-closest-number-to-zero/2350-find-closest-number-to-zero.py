class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]

        for i in range(len(nums)):
            if abs(nums[i]) < abs(ans):
                ans = nums[i]
            elif abs(ans) == abs(nums[i]):
                if ans < nums[i]:
                    ans = nums[i]
        
        return ans

