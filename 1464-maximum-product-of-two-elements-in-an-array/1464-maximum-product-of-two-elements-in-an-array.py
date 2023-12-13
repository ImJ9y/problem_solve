class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxMul = 0
        for i in range(len(nums)):
            curMul = 0
            for j in range(i+1,len(nums)):
                curMul = (nums[i]-1) * (nums[j]-1)
                maxMul = max(curMul, maxMul)
        
        return maxMul