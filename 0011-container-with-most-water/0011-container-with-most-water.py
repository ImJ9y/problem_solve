class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        L, R = 0, len(height)-1

        while L < R:
            min_height = min(height[L], height[R])
            max_area = max(max_area, min_height * (R - L))

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return max_area