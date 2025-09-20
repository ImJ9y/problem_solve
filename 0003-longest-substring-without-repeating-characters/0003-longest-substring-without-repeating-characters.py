class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = 0
        len_sub = 0
        charSet = set()

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                len_sub = max(len_sub, R - L)
                L += 1

            charSet.add(s[R])
    
        return len_sub

