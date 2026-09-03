class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = float('inf')

        while L <= R:
            if nums[L] <= nums[R]:
                return min(nums[L], res)
            
            M = (L + R)//2
            res = min(res, nums[M])

            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M - 1

            
