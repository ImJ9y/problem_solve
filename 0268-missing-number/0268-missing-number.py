class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        print(nums)
        for i in range(len(nums)):
            print(i)
            print(nums[i])
            if nums[i] != i:
                ans = i
                return ans
        
        return len(nums)