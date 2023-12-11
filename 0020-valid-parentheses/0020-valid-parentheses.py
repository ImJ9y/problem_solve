class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        openSymbol = ["(","{","["]
        closeSymbol = [")","}","]"]
        
        if len(s)%2 != 0:
            return False
        
        for symbol in s:
            if symbol in openSymbol:
                temp.append(symbol)
            else:
                if len(temp) == 0:
                    temp.append(symbol)
                elif symbol == "]" and temp[-1] == "[":
                    temp.pop()
                elif symbol == "}" and temp[-1] == "{":
                    temp.pop()
                elif symbol == ")" and temp[-1] == "(":
                    temp.pop()
                else:
                    temp.append(symbol)
        
        return not temp