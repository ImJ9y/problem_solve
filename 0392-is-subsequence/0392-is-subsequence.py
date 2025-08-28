class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        j = 0
        for i in t:
            if j <= len(s)-1 and i == s[j]:
                j += 1
        
        return j == len(s)