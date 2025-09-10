class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        while s[0] == ' ':
            s = s[1:]

        array = []

        start = 0
        i = 0

        while i < len(s):
            while i < len(s) and s[i] != ' ':
                i += 1
            
            if s[start:i] != '':
                array.append(s[start:i])
            
            start = i+1
            i += 1

        return " ".join(array[::-1])

        