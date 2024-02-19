class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            L, R = i+1, len(nums)-1
            
            while L < R:
                threeSum = a + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    ans.append((a, nums[L], nums[R]))
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
            
        return ans
                    
                    