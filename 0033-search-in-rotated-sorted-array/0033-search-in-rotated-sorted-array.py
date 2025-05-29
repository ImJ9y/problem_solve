class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)-1
        ans = -1

        while L <= R:
            M = (L+R)//2

            if nums[M] == target:
                ans = M
                break
            if nums[L] <= nums[M]:
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1

            else:
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        
        return ans
                
