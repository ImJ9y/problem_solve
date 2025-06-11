class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ans = []
        for token in tokens:
            if token not in '+-*/':
                ans.append(int(token))
            else:
                if len(ans) >= 2:
                    b = ans.pop()
                    a = ans.pop()
                    if token == '+':
                        ans.append(a+b)
                    elif token == '-':
                        ans.append(a-b)
                    elif token == '*':
                        ans.append(a*b)
                    elif b != 0 and token == '/':
                        ans.append(int(float(a)/b))
        
        return ans[-1]
        