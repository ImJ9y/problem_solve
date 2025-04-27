class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] #(index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                max_area = max(max_area, stackHeight * (i - stackIndex))
                start = stackIndex
            
            stack.append((start, height))
        
        for i, height in stack:
            max_area = max(max_area, height * (len(heights)-i))
        
        return max_area