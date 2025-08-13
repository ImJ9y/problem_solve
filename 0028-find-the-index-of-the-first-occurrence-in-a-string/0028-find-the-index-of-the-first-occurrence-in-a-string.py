class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L, R = 0, len(needle)

        while R <= len(haystack)+1:
            if haystack[L:R] == needle:
                return L
            L += 1
            R += 1
    
        return -1