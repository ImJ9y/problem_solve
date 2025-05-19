class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height)-1
        max_area = 0

        while L < R:
            cur = min(height[L], height[R]) * (R - L)
            
            if cur > max_area:
                max_area = cur

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_area
