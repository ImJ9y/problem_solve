class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = []

        for operation in operations:
            if len(total) >= 2 and operation == '+':
                total.append(total[-1] + total[-2])
            elif operation == 'D':
                total.append(total[-1]*2)
            elif operation == 'C':
                total.pop()
            else:
                total.append(int(operation))
            
        return sum(total)
            
