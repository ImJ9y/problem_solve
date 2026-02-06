class Solution:
    def minDeletions(self, s: str) -> int:
        char_map = {}
        count = 0

        for i in range(len(s)):
            char_map[s[i]] = 1 + char_map.get(s[i], 0)
        
        unique = set()
        for key, val in char_map.items():
            while val > 0 and val in unique:
                val -= 1
                count += 1
            
            unique.add(val)
        
        return count


            
