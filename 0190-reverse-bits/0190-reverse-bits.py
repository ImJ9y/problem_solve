class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bit = 0
        for _ in range(32):
            reversed_bit = reversed_bit << 1
            bit = n & 1
            reversed_bit = reversed_bit | bit
            n = n >> 1
        
        return reversed_bit
