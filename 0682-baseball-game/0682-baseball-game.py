class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = 0
        score_board = []

        for op in operations:
            score_board.append(op)

            if score_board[-1] == '+':
                score_board.pop()
                new_num = int(score_board[-1]) + int(score_board[-2])
                score_board.append(new_num)

            elif score_board[-1] == 'D':
                score_board.pop()
                double = 2 * int(score_board[-1])
                score_board.append(double)
            
            elif score_board[-1] == 'C':
                score_board.pop()
                score_board = score_board[:-1]
            
            print(score_board)
        
        for score in score_board:
            total += int(score)
        
        return total
