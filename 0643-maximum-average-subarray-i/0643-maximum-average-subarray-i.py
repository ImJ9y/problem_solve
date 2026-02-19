class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_num = sum(nums[:k])
        max_num = cur_num

        L = 0

        for i in range(k, len(nums)):
            cur_num +=  nums[i] - nums[i-k]
            max_num = max(max_num, cur_num)
        
        return max_num / k