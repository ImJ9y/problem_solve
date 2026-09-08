class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        #0000 - 0 - 0

        for i in range(1, n+1):
            print(i//2, i%2)
            res.append(res[i//2] + i%2)
        
        #0001 - 1 - 1
        #0010 - 2 - 1
        #0011 - 3 - 2
        #0100 - 4 - 1

        return res
