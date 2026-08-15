class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #brute force - check every num and find the maximum
        if len(nums) == 1:
            return nums[0]
        
        curr_min_num = 0
        curr_max_num = 0
        max_num = max(nums)

        for num in nums:
            temp = curr_max_num
            curr_max_num = max(num, num * curr_max_num, num*curr_min_num)
            curr_min_num = min(num, num * curr_min_num, num*temp)

            max_num = max(max_num, curr_max_num)

        return max_num
