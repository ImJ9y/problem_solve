class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # char_map1 = {}
        # char_map2 = {}

        # for c in s:
        #     char_map1[c] = 1 + char_map1.get(c, 0)
        
        # for c in t:
        #     char_map2[c] = 1 + char_map2.get(c, 0)

        # return char_map1 == char_map2

        return sorted(s) == sorted(t)