class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        answer = []
        closeToOpen = {")":"(", "}":"{", "]":"["}
        
        for symbol in s:
            if symbol in closeToOpen:
                if answer and answer[-1] == closeToOpen[symbol]:
                    answer.pop()
                else:
                    return False
            else:
                answer.append(symbol)
        
        return not answer
                     
        
        
        