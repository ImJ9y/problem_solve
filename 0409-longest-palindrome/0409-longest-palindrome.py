class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = {}

        count = 0
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
    
            if char_map[c] % 2 == 0:
                count += 2
        
        for _, value in char_map.items():
            if value % 2 == 1:
                count += 1
                break
        
        return count