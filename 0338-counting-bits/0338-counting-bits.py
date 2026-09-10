class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        # 0 = 0000
        # 1 = 0001
        # 2 = 0010
        # 3 = 0011
        # 4 = 0100
        # 5 = 0101
        # 6 = 0110
        # 7 = 0111
        # 8 = 1000

        for i in range(1, n+1):
            res.append(res[i//2] + i%2)
        
        return res