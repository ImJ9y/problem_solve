class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        L = 0
        R = len(height) - 1
        ans = 0
        
        while L < R:
            max_area = (R-L) * min(height[L], height[R])
            ans = max(ans, max_area)
                
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            
        return ans
            

                
                
#         # BRUTE FORCE
#         ans = 0
        
#         for l in range(len(height)):
#             for r in range(l + 1, len(height)):
#                 max_area = (r - l) * min(height[l], height[r])
#                 ans = max(max_area, ans)
        
#         return ans