class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        sum = 0
        count = 0
        
        if "IX" in s :
            sum -= 2
        if "IV" in s:
            sum -= 2
        if "XC" in s:
            sum -= 20
        if "XL" in s:
            sum -= 20
        if "CM" in s:
            sum -= 200
        if "CD" in s:
            sum -= 200
        
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