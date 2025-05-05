class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        L, R = 0, len(nums) - 1
        while L <= R:
            if nums[L] * nums[L] < nums[R] * nums[R]:
                res.append(nums[R] * nums[R])
                R -= 1
            else:
                res.append(nums[L] * nums[L])
                L += 1
        
        return res[::-1]


        # new_array = []

        # for num in nums:
        #     new_array.append(num * num)

        # for i in range(1, len(new_array)):
        #     j = i
        #     while j > 0 and new_array[j-1] > new_array[j]:
        #         new_array[j-1], new_array[j] = new_array[j], new_array[j-1]
        #         j -= 1
        
        # return new_array