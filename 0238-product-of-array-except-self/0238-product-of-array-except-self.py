class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        num_list = [1] * length
        
        for i in range(1, length):    
            num_list[i] = num_list[i-1] * nums[i-1]
        
        R = nums[-1]
        
        print(R)
        print(num_list)
        for i in range(length-2, -1 , -1):
            num_list[i] *= R
            R *= nums[i]
        
        return num_list
        
        
        