class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        LEFT, RIGHT = 0, len(matrix[0])
        TOP, BOTTOM = 0, len(matrix)

        while LEFT < RIGHT and TOP < BOTTOM:
            #get every i in the top row
            for i in range(LEFT, RIGHT):
                output.append(matrix[TOP][i])
            TOP += 1

            #get every i in the right col
            for i in range(TOP, BOTTOM):
                output.append(matrix[i][RIGHT - 1])
            RIGHT -= 1

            if not(LEFT < RIGHT and TOP < BOTTOM):
                break

            #get every i in the bottom row
            for i in range(RIGHT-1, LEFT-1, -1):
                output.append(matrix[BOTTOM -1][i])
            BOTTOM -= 1

            #get every i in the left col
            for i in range(BOTTOM-1, TOP-1, -1):
                output.append(matrix[i][LEFT])
            LEFT += 1
        
        return output