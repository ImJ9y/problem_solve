class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = min(nums)

        while L <= R:
            M = (L + R) //2

            if nums[L] < nums[R]:
                res = min(res, nums[L])
            
            if nums[R] < nums[M]:
                L = M + 1
            else:
                R = M - 1

        return res