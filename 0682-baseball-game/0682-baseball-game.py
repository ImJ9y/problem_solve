class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if stack and op in '+DC':
                if op == '+':
                    stack.append(stack[-1]+stack[-2])
                elif op == 'D':
                    stack.append(stack[-1] * 2)
                elif op == 'C':
                    temp = stack.pop()
            else:
                stack.append(int(op))
            
        return sum(stack)