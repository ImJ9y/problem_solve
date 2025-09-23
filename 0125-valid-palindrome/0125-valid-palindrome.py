class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        L, R = 0, len(new_s)-1
        while L < R:
            if new_s[L] == new_s[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True