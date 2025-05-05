class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""
    

        for c in s:
            if c.isalnum():
                new_string += c.lower()
        
        L, R = 0, len(new_string)-1

        while L < R:
            if new_string[L] == new_string[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True

