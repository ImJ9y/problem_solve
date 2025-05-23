class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_wall, r_wall = 0, 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i -1
            max_left[i] = l_wall
            max_right[j] = r_wall

            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        ans = [0] * n

        for i in range(n):
            possible = min(max_left[i], max_right[i])
            ans[i] = max(0, possible-height[i])
        
        return sum(ans)

        # if not height:
        #     return 0

        # left, right = 0, len(height)-1
        # max_left, max_right = 0, 0
        # trapped_water = 0

        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] >= max_left:
        #             max_left = height[left]
        #         else:
        #             trapped_water += max_left - height[left]

        #         left += 1
        #     else:
        #         if height[right] >= max_right:
        #             max_right = height[right]
        #         else:
        #             trapped_water += max_right - height[right]
                
        #         right -= 1
        
        # return trapped_water
            
