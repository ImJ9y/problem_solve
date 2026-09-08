class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bit = 0

        for _ in range(32):
            reversed_bit = (reversed_bit << 1| n & 1) 
            n = n >> 1
        
        return reversed_bit
1011
    # n = 1

    # reversed = 00
    #bit = 1
    # reversed = 00 | 1 = 1011
