class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
    
        #row
        for i in range(9):
            check_set = set()
            for j in range(9):
                if board[i][j] in check_set:
                    return False
                elif board[i][j] != ".":
                    check_set.add(board[i][j])
        
        #column
        for i in range(9):
            check_set = set()
            for j in range(9):
                if board[j][i] in check_set:
                    return False
                elif board[j][i] != ".":
                    check_set.add(board[j][i])

        #boxes verification
        boxes = [(0,0),(0,3),(0,6),
        (3,0),(3,3),(3,6),
        (6,0),(6,3),(6,6)]

        for box in boxes:
            L, R = box
            check_set = set()
            for row in range(L, L+3):
                for col in range(R, R+3):
                    if board[row][col] in check_set:
                        return False
                    elif board[row][col] != ".":
                        check_set.add(board[row][col])

        return True


        
