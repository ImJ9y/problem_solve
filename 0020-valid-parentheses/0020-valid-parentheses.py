class Solution:
    def isValid(self, s: str) -> bool:
        closed_parenthese = {')':'(', '}':"{",']':'['}
        res = []

        for c in s:
            if c in closed_parenthese:
                if res and res[-1] == closed_parenthese[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        
        return not res
            

