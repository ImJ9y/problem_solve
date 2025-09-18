class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed_symbol = {')':'(', '}':'{',']':'['}
        result = []

        for symbol in s:
            if symbol in closed_symbol:
                if result and closed_symbol[symbol] == result[-1]:
                    result.pop()
                else:
                    return False
            else:
                result.append(symbol)
        
        return not result
