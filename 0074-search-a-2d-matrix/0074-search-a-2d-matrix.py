class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L, R = 0, len(matrix)
        col_L, col_R = 0, len(matrix[0])-1
        while L <= R:
            MID_ROW = (L + R) // 2
            MID_COL = (col_L + col_R) // 2

            print(L, R)
            print(col_L, col_R)

            if MID_ROW < len(matrix) and MID_COL < len(matrix[0]) and matrix[MID_ROW][col_L] <= target and target <= matrix[MID_ROW][col_R]:
                if matrix[MID_ROW][MID_COL] == target:
                    return True
                elif matrix[MID_ROW][MID_COL] < target:
                    col_L = MID_COL + 1
                else:
                    col_R = MID_COL - 1
                print(matrix[MID_ROW][MID_COL])

            elif MID_ROW < len(matrix) and MID_COL < len(matrix[0]) and matrix[MID_ROW][MID_COL] == target:
                return True
            elif MID_ROW < len(matrix) and MID_COL < len(matrix[0]) and matrix[MID_ROW][MID_COL] < target:
                L = MID_ROW + 1
                col_L, col_R = 0, len(matrix[0])-1
            else:
                R = MID_ROW - 1
                col_L, col_R = 0, len(matrix[0])-1
        
        return False

        