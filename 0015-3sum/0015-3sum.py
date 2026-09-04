class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue      
            L = i + 1
            R = len(nums)-1

            while L < R:
                three_sum = nums[i] + nums[L] + nums[R]

                if three_sum < 0:
                    L += 1
                elif three_sum > 0:
                    R -= 1
                else:
                    res.append([nums[i], nums[L], nums[R]])

                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    
                    while R > 0 and nums[R] == nums[R-1]:
                        R -= 1

                    L += 1
                    R -= 1
                    
        return res