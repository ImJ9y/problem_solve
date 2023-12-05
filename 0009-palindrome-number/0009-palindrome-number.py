class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st = str(x)
        if st == st[::-1]:
            return True
        else:
            return False
        