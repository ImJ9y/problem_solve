class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_num = sum(nums[:k])
        max_num = sum_num
        
        for i in range(k, len(nums)):
            sum_num += nums[i] - nums[i-k]
            max_num = max(max_num, sum_num)
        
        return max_num / k