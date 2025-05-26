class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_wall, r_wall = 0,0
        max_l, max_r = [0] * len(height), [0] * len(height)

        for i in range(len(height)):
            j = -i-1

            max_l[i] = l_wall
            max_r[j] = r_wall

            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        ans = [0] * len(height)

        for i in range(len(height)):
            ans[i] += max(0, min(max_l[i], max_r[i]) - height[i])
            
        return sum(ans)