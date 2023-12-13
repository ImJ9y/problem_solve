class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         maxMul = 0
#         for i in range(len(nums)):
#             curMul = 0
#             for j in range(i+1,len(nums)):
#                 curMul = (nums[i]-1) * (nums[j]-1)
#                 maxMul = max(curMul, maxMul)
        
#         return maxMul
        
        biggest = 0
        second_biggest = 0
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
        
        return (biggest - 1) * (second_biggest - 1)
        