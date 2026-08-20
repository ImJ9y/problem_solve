class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall, r_wall = 0, 0
        trapped_water = 0
        L, R = 0, len(height)-1

        while L < R:
            if height[L] < height[R]:
                if l_wall < height[L]:
                    l_wall = height[L]
                else:
                    trapped_water += l_wall - height[L]
                L += 1
            else:
                if r_wall <= height[R]:
                    r_wall = height[R]
                else:
                    trapped_water += r_wall - height[R]
                R -= 1
        
        return trapped_water