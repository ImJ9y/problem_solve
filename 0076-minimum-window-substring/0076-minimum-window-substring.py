class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        result, res_len = [-1,-1], float('inf')
        L = 0

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update our result
                if (R-L+1) < res_len:
                    result =[L, R]
                    res_len = (R - L + 1)
                
                #pop from the left of our window
                window[s[L]] -= 1

                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                
                L += 1
        
        L, R = result
        return s[L:R+1] if res_len != float('inf') else ""                    