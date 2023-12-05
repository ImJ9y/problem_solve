class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        sum = 0
        for symbol in s:
            if symbol == 'M':
                sum += 1000
            elif symbol == 'D':
                sum += 500
            elif symbol == 'C':
                sum += 100
            elif symbol == 'L':
                sum += 50
            elif symbol == 'X':
                sum += 10
            elif symbol == 'V':
                sum += 5
            else:
                sum += 1
        
        return sum