class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)
        
        # if k == 0:
        #     return
        
        # dq = collections.deque(nums)
        
        # for i in range(k):
        #     dq.appendleft(dq[-1])
        #     dq.pop()
        
        # for i in range(len(dq)):
        #     nums[i] = dq[i]

        k = k % len(nums) #look for the reminder of nums length

        nums[:] = nums[-k:] + nums[:-k]