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

        while n:
            if isBadVersion(n):
                n -= 1
            else:
                return n+1
        
        return n+1