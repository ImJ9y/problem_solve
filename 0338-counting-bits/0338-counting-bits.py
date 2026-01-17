class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def countbit(n):
            count = 0
            while n > 0:
                count += n & 1
                n >>= 1
            
            return count
        
        for i in range(n+1):
            ans.append(countbit(i))
        
        return ans
