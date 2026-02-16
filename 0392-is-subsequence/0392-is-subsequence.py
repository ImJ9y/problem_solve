class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = max(len(s), len(t))
        
        j = 0
        for i in range(length):
            if j < len(s) and i < len(t) and s[j] == t[i]:
                j += 1
        
        return len(s) == j