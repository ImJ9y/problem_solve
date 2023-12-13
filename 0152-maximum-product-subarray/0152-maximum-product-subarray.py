class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        currMin, currMax = 1,1
        
        
        for num in nums:
            #0 is netural -> need to refresh the min and max
            
            if num == 0:
                currMin, currMax = 1,1

            #when we use num*currMax in currMin - the value is changing
            #so we are going to generate new object to generate previous num*currMax
            temp = num * currMax
            currMax = max(num, num*currMin, num*currMax)
            currMin = min(num, num*currMin, temp)
            
            maxNum = max(maxNum, currMax)
        
        return maxNum
            