class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        ans = [''] * numRows
        row = 0
        i = 0

        for c in s:
            row += i

            if row == numRows-1:
                i = -1
            if row == 0:
                i = 1
            
            ans[row] += c

        result = ""

        for s in ans:
            result += "".join(s)
        
        return result
            