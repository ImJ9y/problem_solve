class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checkList = []
        openSymbol = ["(","[","{"]
        closeSymbol = [")","]","}"]
        
        if len(s) % 2 != 0:
            return False
        
        for symbol in s:
            if symbol in openSymbol:
                checkList.append(symbol)
            else:
                if len(checkList) == 0:
                    return False
                elif checkList[-1] == "{" and symbol == "}":
                    checkList.pop()
                elif checkList[-1] == "[" and symbol == "]":
                    checkList.pop()
                elif checkList[-1] == "(" and symbol == ")":
                    checkList.pop()
                elif symbol in closeSymbol:
                    checkList.append(symbol)
        
        return not checkList
            
                    
                            
        