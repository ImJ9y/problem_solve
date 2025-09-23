class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #Row verification
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        #Column verificaiton
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        #box verification
        starts = [(0,0), (0,3), (0,6),
         (3,0), (3,3), (3,6),
         (6,0), (6,3), (6,6) ]
        
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
    
        return True



