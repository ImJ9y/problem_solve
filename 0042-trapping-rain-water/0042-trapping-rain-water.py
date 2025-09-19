class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_l, max_r = 0, 0
        L, R = 0, len(height)-1
        trapped_water = 0

        while L < R:
            if height[L] < height[R]:
                if max_l <= height[L]:
                    max_l = height[L]
                else:
                    trapped_water += min(max_l, max_l - height[L])
                L += 1
            else:
                if max_r <= height[R]:
                    max_r = height[R]
                else:
                    trapped_water += min(max_r, max_r - height[R])
                R -= 1
        
        return trapped_water