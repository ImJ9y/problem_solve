class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checkList = []
        openSymbol = ["(","{","["]
        closeSymbol = [")","}","]"]
        
        if len(s)%2 != 0:
            return False
        
        
        for symbol in s:
            if symbol in openSymbol:
                checkList.append(symbol)
            else:
                if len(checkList) == 0:
                    checkList.append(symbol)
                elif symbol == "]" and checkList[-1] == "[":
                    checkList.pop()
                elif symbol == "}" and checkList[-1] == "{":
                    checkList.pop()
                elif symbol == ")" and checkList[-1] == "(":
                    checkList.pop()
                else:
                    checkList.append(symbol)
        
        return not checkList
                    
            