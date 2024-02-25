class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        count = 0
        for i in range(n+1):
            for j in bin(i):
                if '1' in j:
                    count += 1
            ans.append(count)
            count = 0
        
        return ans
        