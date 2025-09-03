class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height)-1
        most_water = 0

        while L < R:
            cur = min(height[L], height[R]) * (R - L)
            if most_water < cur:
                most_water = cur
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return most_water

            