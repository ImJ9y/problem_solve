class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        new_s = str(x)

        return new_s == new_s[::-1]