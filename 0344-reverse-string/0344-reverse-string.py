class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s)-1

        while L < R:
            s[L],s[R] = s[R],s[L]
            L += 1
            R -= 1

            