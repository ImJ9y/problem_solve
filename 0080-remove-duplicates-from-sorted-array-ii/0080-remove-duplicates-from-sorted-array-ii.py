class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First, identify the distinct values and remove extra duplicates.
        # k = 1
        # for i in range(1, len(nums)):
        #     if nums[i-1] != nums[i]:
        #         nums[k] = nums[i]
        #         k += 1
        
        # print(nums)
        # return k

        # Next, allow up to two occurrences of each element in the list.
        k = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k


        