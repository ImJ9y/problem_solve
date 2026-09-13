class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bit(n):
            res = 0
            while n:
                if n&1:
                    res += 1
                n >>= 1
            return res

        res = [0]
        for i in range(1,n+1):
            res.append(count_bit(i))
        
        return res
