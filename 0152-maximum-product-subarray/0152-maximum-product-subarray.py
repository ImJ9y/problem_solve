class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num, max_num = 1,1
        max_product = max(nums)
        
        for n in nums:
            temp = max_num * n
            max_num = max(min_num * n, max_num * n, n)
            min_num = min(min_num * n, temp, n)
            max_product = max(max_num, min_num, max_product)
            
        return max_product