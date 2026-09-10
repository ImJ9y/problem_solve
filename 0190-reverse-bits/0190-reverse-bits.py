class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bit = 0

        for _ in range(32):
            reversed_bit = (reversed_bit << 1) | n & 1
            n >>= 1
        
        return reversed_bit