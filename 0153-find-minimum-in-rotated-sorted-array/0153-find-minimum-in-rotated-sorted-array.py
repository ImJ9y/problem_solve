class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, len(nums) -1
        answer = 0
        
        if len(nums) == 1:
            return nums[0]
        
        while L < R:
            answer = min(nums[L], nums[R])
            M = (L+R)/2
            answer = min(answer, nums[M])
            
            if nums[M] < nums[R]:
                R -= 1
            else:
                L += 1
            
        return answer
            