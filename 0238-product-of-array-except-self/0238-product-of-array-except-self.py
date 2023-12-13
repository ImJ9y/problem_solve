class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length

        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]
        
        Right = nums[-1] #generating the last value of Nums List
        
        for i in range(length-2, -1,-1):
            answer[i] *= Right #Multiple the number from list to Answer
            Right *= nums[i] #Next number from the list
            
        return answer