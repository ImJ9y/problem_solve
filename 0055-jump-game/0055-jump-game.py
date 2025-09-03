class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            #i = your current position.
            #nums[i] = how far you can jump forward from there.
            #So i + nums[i] = the furthest index you can reach if you jump from i.
            farthest = i + nums[i]
            

            if farthest >= goal:
                goal = i
        
        return goal == 0