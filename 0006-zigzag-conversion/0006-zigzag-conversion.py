class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        down = 0
        row = 0
        ans = [''] * numRows

        for c in s:
            ans[row] += c

            if row == numRows-1:
                down = -1
            if row == 0:
                down = 1
            
            row += down

        result = ""
        for st in ans:
            result += "".join(st)
        
        return result
            
