class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            L = i + 1
            R = len(nums)-1

            while L < R:
                cur = n + nums[L] + nums[R]

                if cur < 0:
                    L += 1
                elif cur > 0:
                    R -= 1
                else:
                    res.append([n, nums[L], nums[R]])

                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while R > L and nums[R] == nums[R-1]:
                        R -= 1
                    
                    L += 1
                    R -= 1
        
        return res
