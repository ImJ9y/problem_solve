class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strNum = str(x)
        convertToStr = ""

        for num in strNum[::-1]:
            convertToStr += num
        
        return strNum == convertToStr