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
        
        return new_s == new_s[::-1]