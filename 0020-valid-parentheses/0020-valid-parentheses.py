class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []

        closed_brackets = {')':'('
                          ,']':'['
                          ,'}':'{'}

        
        for b in s:
            if b in closed_brackets:
                if ans and ans[-1] == closed_brackets[b]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(b)
        
        return True if not(ans) else False

            