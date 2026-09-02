class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            L = i+1
            R = len(nums)-1

            while L < R:
                threeSum = nums[i] + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])

                    while L < len(nums)-1 and nums[L] == nums[L+1]:
                        L += 1
                        continue
                    
                    while R > 0 and nums[R] == nums[R-1]:
                        R -= 1
                        continue
                    L += 1
                    R -= 1
        return res
