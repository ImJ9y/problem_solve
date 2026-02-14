class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        unique = set()

        for num in arr:
            seen[num] = 1 + seen.get(num, 0)
        
        for key, val in seen.items():
            if val in unique:
                return False
            unique.add(val)
        
        return True