class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_s = {}
        count = 0
        
        for c in s:
            char_s[c] = char_s.get(c, 0) + 1
            if char_s[c] % 2 == 0:
                count += 2
        
        for _, value in char_s.items():
            if value % 2 == 1:
                count += 1
                break

        return count
