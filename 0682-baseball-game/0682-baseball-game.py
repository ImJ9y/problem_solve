class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = 0
        score_board = []

        for op in operations:
            if op == '+':
                score_board.append(score_board[-1] + score_board[-2])
            elif op == 'D':
                score_board.append(2 * score_board[-1])
            elif op == 'C':
                score_board.pop()
            else:
                score_board.append(int(op))
        
        return sum(score_board)
