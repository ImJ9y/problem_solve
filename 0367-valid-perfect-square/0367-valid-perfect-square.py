class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root = int((num**.5))

        return True if (root * root) == num else False
        