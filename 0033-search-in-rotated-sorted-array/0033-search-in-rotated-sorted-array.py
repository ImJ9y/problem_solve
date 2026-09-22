class Solution:
    def search(self, nums: list[int], target: int) -> int:
        res = -1
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L+R)//2
            if nums[M] == target:
                res = M
                return res
            
            if nums[L] <= nums[M]:
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if nums[R] >= target > nums[M]:
                    L = M + 1
                else:
                    R = M - 1

        return res