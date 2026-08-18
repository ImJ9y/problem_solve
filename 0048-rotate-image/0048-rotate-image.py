class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        LEFT, RIGHT = 0, len(matrix)-1

        while LEFT < RIGHT:
            for i in range(RIGHT-LEFT):
                TOP, BOTTOM = LEFT, RIGHT
                TOPLEFT = matrix[TOP][LEFT + i]
                matrix[TOP][LEFT + i] = matrix[BOTTOM - i][LEFT]
                matrix[BOTTOM - i][LEFT] = matrix[BOTTOM][RIGHT - i]
                matrix[BOTTOM][RIGHT - i] = matrix[TOP + i][RIGHT]
                matrix[TOP + i][RIGHT] = TOPLEFT
            
            LEFT += 1
            RIGHT -= 1


        # n = len(matrix)
        
        # # Step 1: Transpose the matrix
        # for i in range(n):
        #     # 0 1 2 
        #     for j in range(i + 1, n):
        #         # 1 2
        #         print(matrix[i][j], matrix[j][i])
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # # Step 2: Reverse each row
        # for i in range(n):
        #     matrix[i].reverse()