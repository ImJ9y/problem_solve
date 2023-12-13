class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        
        #hello
        #ll
        #he, el, ll, lo, o... (only 4)
        #searching until right before last character of haystack
        for i in range(len(haystack)+1 - len(needle)):       
            #move next character after searching length of needle
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1        
        
        
#         if haystack == needle:
#             return 0
        
#         for i in range(len(haystack)):
#             if haystack[i:len(needle)+i] == needle:
#                 return i
        
#         return -1
            