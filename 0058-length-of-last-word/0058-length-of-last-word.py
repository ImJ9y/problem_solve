class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s[-1] == " ":
            s = s[:-1]
        
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                return count
            
            count += 1
        
        return count