class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        res = 0
        L = 0
        count_bank = {}

        for R in range(len(s)):
            count_bank[s[R]] = 1 + count_bank.get(s[R],0)
            max_freq = max(max_freq, count_bank[s[R]])

            while R - L + 1 - max_freq > k:
                count_bank[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
        
        return res