class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Left = 0
        Right = len(nums) -1
        
        while Left <= Right:
            mid = (Left + Right) // 2
            
            if nums[mid] == target:
                return mid
            
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[Left]: # left rotated
                # in ascending order side
                if nums[Left] <= target and target < nums[mid]:
                    Right = mid - 1
                else:
                    Left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[Right]:
                    Left = mid + 1
                else:
                    Right = mid - 1
        # cannot find the target value
        return -1
            