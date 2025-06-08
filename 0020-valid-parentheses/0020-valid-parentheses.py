class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed_brackets = {')':'(','}':'{',']':'['}
        res = []


        for c in s:
            if c in closed_brackets:
                if res and res[-1] == closed_brackets[c]:
                    res.pop()
                else:
                    res.append(c)
            else:
                res.append(c)
        
        return not res
        