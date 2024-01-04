class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        result = []
        str_digits = ''.join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        for i in str_digits:
            result.append(int(i))
        
        return result
    

#         length = len(digits) - 1
#         while digits[length] == 9:
#             digits[length] = 0
#             length -= 1
#         if(length < 0):
#             digits = [1] + digits
#         else:
#             digits[length] += 1
 
#         return digits