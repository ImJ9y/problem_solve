class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        sum = 0
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL','XXXX').replace('XC', 'LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        for letter in s:
            if letter == "M":
                sum += 1000
            elif letter == "D":
                sum += 500
            elif letter == "C":
                sum += 100
            elif letter == "L":
                sum += 50
            elif letter == "X":
                sum += 10
            elif letter == "V":
                sum += 5
            elif letter == "I":
                sum += 1
            else:
                continue
        
        return sum