class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            LEFT = i + 1
            RIGHT = len(nums)-1

            while LEFT < RIGHT:
                cur = nums[i] + nums[LEFT] + nums[RIGHT]

                if cur < 0:
                    LEFT += 1
                elif cur > 0:
                    RIGHT -= 1
                else:
                    res.append([nums[i], nums[LEFT], nums[RIGHT]])

                    while LEFT < RIGHT and nums[LEFT] == nums[LEFT+1]:
                        LEFT += 1
                    
                    while RIGHT > 0 and nums[RIGHT] == nums[RIGHT-1]:
                        RIGHT -= 1
                    
                    LEFT += 1
                    RIGHT -= 1
            
        return res
                    