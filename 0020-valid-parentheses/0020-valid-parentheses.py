class Solution:
    def isValid(self, s: str) -> bool:
        closed_p = {')':'(','}':'{',']':'['}
        res = []

        for i in range(len(s)):
            if s[i] in closed_p:
                print(closed_p[s[i]])
                if res and res[-1] == closed_p[s[i]]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])

        return not res
            

