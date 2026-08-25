class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_c = defaultdict(int)

        res = 0
        for c in s:
            char_c[c] += 1
            if char_c[c] % 2 == 0:
                res += 2
        
        for c in s:
            if char_c[c] % 2 == 1:
                res += 1
                break
        
        return res
        