class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        L, R = 0, len(new_str)-1

        while L < R:
            if new_str[L] == new_str[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True