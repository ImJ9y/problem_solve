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
        
        L, R = 0, len(res)-1
        while L < R:
            if res[L] == res[R]:
                L += 1
                R -= 1
            else:
                return False
        return True

        # return res == res[::-1]
