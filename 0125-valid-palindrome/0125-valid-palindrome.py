class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ans = ""
        for c in s:
            if c.isalnum():
                ans += c.lower()
        
        return ans == ans[::-1]