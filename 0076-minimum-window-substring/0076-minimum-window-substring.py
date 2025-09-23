class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if t == "": return ""

        countT, window ={}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        result, result_len = [-1, -1], float('inf')

        have, need = 0, len(countT)
        L = 0

        for R in range(len(s)):
            cur_c = s[R]
            window[cur_c] = 1 + window.get(cur_c, 0)

            if cur_c in countT and window[cur_c] == countT[cur_c]:
                have += 1
            
            while need == have:
                #result update
                if R - L + 1 < result_len:
                    result_len = R - L + 1
                    result = [L, R]

                #pop left
                window[s[L]] -= 1

                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
            
                L += 1
        
        L, R = result

        return s[L:R+1] if result_len != float('inf') else ""
            
