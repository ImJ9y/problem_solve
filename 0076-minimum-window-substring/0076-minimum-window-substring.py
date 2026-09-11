class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_T, window = {}, {}

        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)
        
        have, need = 0, len(count_T)
        L = 0
        res, res_len = [-1,-1], float('inf')

        for R in range(len(s)):
            cur_c = s[R]
            window[cur_c] = 1 + window.get(cur_c, 0)

            if cur_c in count_T and window[cur_c] == count_T[cur_c]:
                have += 1

                while have == need:
                    if R - L + 1 < res_len:
                        res = [L, R]
                        res_len = R - L + 1
                    
                    window[s[L]] -= 1
                    
                    if s[L] in count_T and window[s[L]] < count_T[s[L]]:
                        have -= 1
                    
                    L += 1

        L, R = res

        return s[L:R+1] if res_len != float('inf') else ""
