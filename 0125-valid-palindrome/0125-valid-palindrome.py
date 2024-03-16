class Solution(object):
    def alphaNum(self, c):
       return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
#         ans = ""
#         for c in s:
#             if c.isalnum():
#                 ans += c.lower()
        
#         return ans == ans[::-1]
    
        L, R = 0, len(s)-1
    
        while L < R:
            while L < R and not self.alphaNum(s[L]):
                L += 1
            while R > L and not self.alphaNum(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False

            L, R = 1 + L, R -1

        return True

    
            