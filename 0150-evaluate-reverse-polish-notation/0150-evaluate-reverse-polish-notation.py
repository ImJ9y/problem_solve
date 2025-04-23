class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/' and b != 0:
                    # Integer division toward zero
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))

        return stack[-1]