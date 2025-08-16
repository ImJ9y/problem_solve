class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = []

        for val, symbol in value_symbols:
            
            count = num // val
            result.append(symbol * count)
            num -= val * count
        
        return "".join(result)



        
        

