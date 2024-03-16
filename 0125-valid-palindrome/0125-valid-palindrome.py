class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ans = ""
        for c in s:
            if c.isalnum():
                ans += c
        
        return ans.lower() == ans[::-1].lower()