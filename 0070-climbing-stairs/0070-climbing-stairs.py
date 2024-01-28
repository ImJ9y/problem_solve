class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
#          #Brute Force
#         one, two = 1,1
        
#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp
            
#         return one

        if n == 1:
            return 1
        
        if n == 2:
            return 2

        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]