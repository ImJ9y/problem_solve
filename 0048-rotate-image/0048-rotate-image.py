class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        LEFT, RIGHT = 0, len(matrix)-1

        while LEFT < RIGHT:
            TOP, BOTTOM = LEFT, RIGHT
            for i in range(RIGHT - LEFT):
                TOPLEFT = matrix[TOP][LEFT+i]

                matrix[TOP][LEFT+i] = matrix[BOTTOM-i][LEFT]

                matrix[BOTTOM-i][LEFT] = matrix[BOTTOM][RIGHT-i]

                matrix[BOTTOM][RIGHT-i] = matrix[TOP+i][RIGHT]

                matrix[TOP+i][RIGHT] = TOPLEFT

            LEFT += 1
            RIGHT -= 1




