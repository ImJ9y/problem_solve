class Solution:
    def reverseBits(self, n: int) -> int:
        bit = n
        res = ""
        while bit:
            res += str(bit%2)
            bit = bit//2

        extra_zero = 32 - len(res)
        res += '0' * extra_zero

        
        ans = 0
        res_list = list(res)
        for i in range(len(res_list)-1,-1,-1):
            ans += int(res_list[i]) * (2 ** (31 - i))

        return ans