class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0

        L, R = 0, len(height)-1

        while L < R:
            cur_area = min(height[L], height[R]) * (R-L)
            if max_area < cur_area:
                max_area = cur_area
            else:
                if height[L] < height[R]:
                    L += 1
                else:
                    R -= 1
        
        return max_area