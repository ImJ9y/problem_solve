class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        currMin, currMax = 1, 1
        maxNum = max(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                
            temp = num * currMax
            currMax = max(num, num*currMin, num*currMax)
            currMin = min(num, num*currMin, temp)
        
            maxNum = max(maxNum, currMax)
        
        return maxNum