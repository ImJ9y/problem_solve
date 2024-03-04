class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = 0
        R = len(nums)-1
        answer = 0
        
        if len(nums) == 1:
            return nums[0]
        
        
        while L <= R:
            answer = min(nums[L], nums[R])
            
            M = (L+R)/2
            answer = min(answer, nums[M])
            
            if nums[R] < nums[M]:
                L += 1
            else:
                R -= 1
        
        return answer
                
                
          