class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        dp = collections.deque(nums)

        for i in range(k):
            temp = dp.pop()
            dp.appendleft(temp)

        for i in range(len(nums)):
            nums[i] = dp[i]

        # k = k%len(nums)
        # nums[:] = nums[-k:] + nums[:-k]