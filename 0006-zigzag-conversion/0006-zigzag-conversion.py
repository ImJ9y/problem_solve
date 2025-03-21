class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]
        
        i = 0
        dep = 0

        for char in s:
            if i == numRows-1:
                dep = -1
            if i == 0:
                dep = 1
            
            ans[i].append(char)
            i += dep

        result = ""
        for s in ans:
            result += "".join(s)
        
        return result
            
