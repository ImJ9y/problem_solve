class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # root = int((num**.5))

        # return True if (root * root) == num else False

        L, R = 1, num
        while L <= R:
            M = (L+R)//2

            if M * M > num:
                R = M - 1
            elif M * M < num:
                L = M + 1
            else:
                return True
        
        return False

        