class Solution:
    def minDeletions(self, s: str) -> int:
        char_map = {}
        used_freq = set()
        count = 0

        for c in s:
            char_map[c] = 1 + char_map.get(c, 0)
        
        used_freq = set()
        
        for key, val in char_map.items():
            while val > 0 and val in used_freq:
                val -= 1
                count += 1
            
            used_freq.add(val) #unique or 0
            
        return count