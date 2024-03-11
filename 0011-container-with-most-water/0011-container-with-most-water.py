class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = 0
        R = len(height)-1
        ans = 0
        
        while L < R:
            max_area = (R-L) * min(height[L], height[R])
            ans = max(ans, max_area)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return ans
        