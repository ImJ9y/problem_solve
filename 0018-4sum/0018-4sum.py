class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                L = j + 1
                R = len(nums)-1

                while L < R:
                    cur = nums[i] + nums[j] + nums[L] + nums[R]

                    if cur < target:
                        L += 1
                    elif cur > target:
                        R -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])

                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -= 1
                        
                        L += 1
                        R -= 1
        
        return ans