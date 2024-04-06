class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = 0
        R = len(height)-1
        max_area = 0
        
        while L < R:
            area = (R-L) * min(height[L], height[R])
            max_area = max(max_area, area)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_area
            