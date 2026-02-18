class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * (len(gain)+1)
        res[0] = 0

        for i in range(1,len(gain)+1):
            res[i] = res[i-1] + gain[i-1]
        
        return max(res)