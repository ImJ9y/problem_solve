class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed_brackets = {")":"(","}":"{","]":"["}
        stack = []

        for bracket in s:
            if stack and bracket in closed_brackets:
                if stack[-1] == closed_brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return not stack