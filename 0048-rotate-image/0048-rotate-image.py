class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        LEFT, RIGHT = 0, len(matrix[0])-1
        
        while LEFT < RIGHT:
            TOP, BOTTOM = LEFT, RIGHT
            for i in range(RIGHT-LEFT):
                #store the TOPLEFT value
                TOPLEFT = matrix[TOP][LEFT+i]
                
                #insert TOPLEFT from BOTTOM LEFT
                matrix[TOP][LEFT+i] = matrix[BOTTOM-i][LEFT]

                #insert BOTTOM LEFT from BOTTOM RIGHT
                matrix[BOTTOM-i][LEFT] = matrix[BOTTOM][RIGHT-i]

                #insert BOTTOM RIGHT from TOP RIGHT
                matrix[BOTTOM][RIGHT-i] = matrix[TOP+i][RIGHT]

                #insert TOP RIGHT from TOP LEFT
                matrix[TOP+i][RIGHT] = TOPLEFT
            
            LEFT += 1
            RIGHT -= 1
