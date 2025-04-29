class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = [] #[i, height]

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                stackindex, stackheight = stack.pop()
                max_area = max(max_area, stackheight * (i-stackindex))
                start = stackindex

            stack.append([start, height])

        for i, height in stack:
            max_area = max(max_area, height * (len(heights)-i))

        
        return max_area