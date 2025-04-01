class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)

        j = 0
        for i in range(T):
            if j < S and s[j] == t[i]:
                j += 1

        return j == S
            
