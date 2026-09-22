class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]

        for i in range(1, n+1):
            res.append(res[i//2] + i%2)
        return res
        
        # def helper(n):
        #     count = 0
        #     while n:
        #         if n & 1:
        #             count += 1
                
        #         n >>= 1

        #     return count

        # res = [0]    
        # for i in range(1, n+1):
        #     res.append(helper(i))
        
        # return res