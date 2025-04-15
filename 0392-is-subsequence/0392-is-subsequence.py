class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)

        i = 0

        for j in range(len(t)):
            if i < S and s[i] == t[j]:
                i += 1
        
        return S == i