# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 0, n

        while L < R:
            M = (L+R)//2

            if isBadVersion(M):
                R = M
            else:
                L = M + 1
        
        return R