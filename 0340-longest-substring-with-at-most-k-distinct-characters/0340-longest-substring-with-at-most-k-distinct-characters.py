class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        L, R = 0, 0
        n = len(s)
        char_map = {}

        while R < n:
            char_map[s[R]] = char_map.get(s[R], 0) + 1

            while len(char_map) > k:
                char_map[s[L]] -= 1
                if char_map[s[L]] == 0:
                    char_map.pop(s[L])
                L += 1
            
            longest = max(longest, R - L + 1)
            R += 1
        
        return longest