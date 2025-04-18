class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        LEFT, RIGHT = 0, len(matrix[0])-1

        while LEFT < RIGHT:
            for i in range(RIGHT-LEFT):
                TOP, BOTTOM = LEFT, RIGHT

                #Save TOP LEFT value
                TOPLEFT = matrix[TOP][LEFT+i]

                #Save BOTTOM LEFT value to TOP LEFT
                matrix[TOP][LEFT+i] = matrix[BOTTOM-i][LEFT]

                #Save BOTTOM RIGHT value to BOTTOM LEFT
                matrix[BOTTOM-i][LEFT] = matrix[BOTTOM][RIGHT-i]

                #Save TOP RIGHT value to BOTTOM RIGHT
                matrix[BOTTOM][RIGHT-i] = matrix[TOP+i][RIGHT]

                #Save TOP LEFT value to TOP RIGHT
                matrix[TOP+i][RIGHT] = TOPLEFT

            LEFT += 1
            RIGHT -= 1