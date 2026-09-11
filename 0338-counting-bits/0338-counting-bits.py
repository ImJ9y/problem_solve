class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bit(n):
            count = 0
            while n:
                count += n&1
                n >>= 1
            
            return count
        
        res = [0]
        
        for i in range(1, n+1):
            res.append(count_bit(i))
    
        return res
        
        