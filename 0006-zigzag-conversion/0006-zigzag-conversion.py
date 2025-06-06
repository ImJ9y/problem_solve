class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        row = 0
        ans = [""] * numRows
        i = 1
        for c in s:
            ans[row] += c
            if row == numRows-1:
                i = -1
            if row == 0:
                i = 1
            
            row += i
        
        res = ""
        for new_s in ans:
            res += "".join(new_s)
    
        return res