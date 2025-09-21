class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        L, R = 0, len(height)-1
        area = 0

        while L < R:
            area = max(area, (min(height[L], height[R]) * (R - L)))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return area