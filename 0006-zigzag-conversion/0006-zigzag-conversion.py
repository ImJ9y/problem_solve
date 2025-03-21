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
        row = 0
        j = 0
        for i in range(len(s)):
            j = j + row
            ans[j].append(s[i])

            if j == 0:
                row = 1
            if j == numRows-1:
                row = -1

        result = ""

        for s in ans:
            result += "".join(s)
        
        return result
            
