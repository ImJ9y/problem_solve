class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i+1, len(nums)-1

            while L < R:
                cur = nums[i] + nums[L] + nums[R]

                if cur < 0:
                    L += 1
                elif cur > 0:
                    R -= 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])

                    while L < len(nums)-1 and nums[L] == nums[L+1]:
                        L += 1
                    
                    while R > 0 and nums[R] == nums[R-1]:
                        R -= 1
                    
                    L += 1
                    R -= 1
                
        return ans