class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        hl = len(haystack)
        nl = len(needle)

        for i in range(0,hl-nl+1,1):       
            if haystack[i:i+nl] == needle:
                return i

        return -1        
        
        
#         if haystack == needle:
#             return 0
        
#         for i in range(len(haystack)):
#             if haystack[i:len(needle)+i] == needle:
#                 return i
        
#         return -1
            