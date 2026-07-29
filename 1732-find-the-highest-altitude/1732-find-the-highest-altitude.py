class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = 0
        cur = 0
        for g in gain:
            cur += g
            max_gain = max(max_gain, cur)
        
        return max_gain