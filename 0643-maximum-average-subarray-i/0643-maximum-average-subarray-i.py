class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_num = sum(nums[:k])
        max_num = sum_num

        L = 0
        for i in range(k, len(nums)):
            sum_num += nums[i]
            sum_num -= nums[L]
            max_num = max(max_num, sum_num)
            L += 1
        
        return max_num / k