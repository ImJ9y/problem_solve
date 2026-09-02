class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        res = 0
        L = 0


        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            max_freq = max(max_freq, count[s[R]])

            if R - L + 1 - max_freq > k:
                count[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)

        return res
