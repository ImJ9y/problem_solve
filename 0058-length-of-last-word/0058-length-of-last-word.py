class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        R = len(s)-1
        
        while s[R] == " ":
            R -= 1
        

        L = R

        while L >= 0 and s[L] != " ":
            L -= 1
        
        return R - L

        #return len(s.split()[-1])