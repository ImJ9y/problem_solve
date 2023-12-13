class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        if len(num) < 3:
            return ""
        
        maxNum = []
        result = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                maxNum.append(num[i])

        
        if maxNum:
            result = max(maxNum)
        else:
            return ""
    
        return result*3