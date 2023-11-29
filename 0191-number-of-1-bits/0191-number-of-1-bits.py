class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #can update int to binary
        # print(bin(n))
        # print('{0:b}'.format(n))
        
        sum = 0
        stringNum = bin(n)
        for o in stringNum:
            if o == "1":
                sum += 1
        
        return sum