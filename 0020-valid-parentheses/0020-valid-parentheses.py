
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checkList = []
        openSymbol = ["(","[","{"]
        closeSymbol = [")","]","}"]

        if len(s)%2 != 0:
            return False
        else:
            for symbol in s:
                if symbol in openSymbol:
                    checkList.append(symbol)
                else:
                    if len(checkList) == 0:
                        checkList.append(symbol)
                    elif symbol in closeSymbol:
                        if checkList[-1] == "{" and symbol == "}":
                            checkList.pop()
                        elif checkList[-1] == "[" and symbol == "]":
                            checkList.pop()
                        elif checkList[-1] == "(" and symbol == ")":
                            checkList.pop()
                        else:
                            checkList.append(symbol)

        return not checkList