class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_l, max_r = 0, 0
        water_contained = 0
        L, R = 0, len(height)-1

        while L <= R:
            
            if height[L] <= height[R]:
                if height[L] > max_l:
                    max_l = max(max_l, height[L])
                if height[R] > max_r:
                    max_r = max(max_r, height[R])
                L += 1
            
            else:
                if height[L] >= max_l:
                    max_l = max(max_l, height[L])
                if height[R] > max_r:
                    max_r = max(max_r, height[R])
                
                R -= 1
            
            water_contained = max(water_contained, min(max_l, max_r) * (R - L + 1))
        
        return water_contained
