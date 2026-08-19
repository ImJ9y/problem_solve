class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = 0
        L = 0
        res = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxFreq = max(maxFreq, count[s[R]])

            while R - L + 1 - maxFreq > k:
                count[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
        
        return res