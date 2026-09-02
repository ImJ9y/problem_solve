class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = float('inf')

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            M = (L + R) //2
            if nums[R] > nums[M]:
                R = M - 1
            else:
                L = M + 1

        return res