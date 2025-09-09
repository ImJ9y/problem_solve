class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_symbols = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }

        ans = 0

        for i in range(1, len(s)+1):
            if i < len(s) and value_symbols[s[i-1]] < value_symbols[s[i]]:
                ans -= value_symbols[s[i-1]]
            else:
                ans += value_symbols[s[i-1]]
        
        return ans
