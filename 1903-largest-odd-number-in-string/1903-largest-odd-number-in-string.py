class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        indx = -1
        for i in range(0,len(num)):
            if int(num[i]) % 2 != 0:
                indx = i
                
        if indx == -1:
            return ""
        else:
            return num[:indx+1]
        