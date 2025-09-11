class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        array = [''] * numRows
        row = 0
        i = 0

        for c in s:
            row += i
            array[row] += c

            if row == 0:
                i = 1
            if row == numRows-1:
                i = -1
        
        new_s = ""

        for s in array:
            new_s += "".join(s)
        
        return new_s