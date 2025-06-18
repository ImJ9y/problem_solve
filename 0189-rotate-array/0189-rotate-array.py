class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # new_nums = collections.deque(nums)

        # for i in range(k):
        #     temp = new_nums.pop()
        #     new_nums.appendleft(temp)
        
        # for i in range(len(new_nums)):
        #     nums[i] = new_nums[i]