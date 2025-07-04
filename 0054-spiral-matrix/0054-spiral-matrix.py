class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        TOP, BOTTOM = 0, len(matrix)
        LEFT, RIGHT = 0, len(matrix[0])

        ans = []

        while LEFT < RIGHT and TOP < BOTTOM:
            for i in range(LEFT, RIGHT):
                ans.append(matrix[TOP][i])
            TOP += 1

            for i in range(TOP, BOTTOM):
                ans.append(matrix[i][RIGHT-1])
            RIGHT -= 1

            if not(LEFT < RIGHT and TOP < BOTTOM):
                break

            for i in range(RIGHT-1, LEFT-1, -1):
                ans.append(matrix[BOTTOM-1][i])
            BOTTOM -= 1
    
            for i in range(BOTTOM-1, TOP-1, -1):
                ans.append(matrix[i][LEFT])
            LEFT += 1

        return ans