class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        while s[-1] == " ":
            s = s[:-1]
        
        if len(s) == 1:
            return 1
        
        index = 0
        for i in range(len(s)):
            if s[i] == ' ':
                index = i + 1
        return len(s[index:])