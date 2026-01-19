class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        def count_b(n):
            count = 0

            while n > 0:
                count += n&1
                n >>= 1
        
            return count
        
        ans = []

        for i in range(n+1):
            ans.append(count_b(i))
        
        return ans
