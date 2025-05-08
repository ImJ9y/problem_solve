class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""

        for c in s:
            if c.isalnum():
                res += c.lower()
        
        return res == res[::-1]
