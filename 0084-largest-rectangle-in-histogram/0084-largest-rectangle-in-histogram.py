class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                stk_index, stk_height = stack.pop()
                max_area = max(stk_height * (i - stk_index), max_area)
                start = stk_index
            stack.append([start, height])
        
        for i, height in stack:
            max_area = max(max_area, (height * (len(heights)-i)))

        return max_area
        