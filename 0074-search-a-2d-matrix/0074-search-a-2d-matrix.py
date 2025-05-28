class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            L, R = 0, len(matrix[i])

            while L < R:
                M = (L+R)//2

                if matrix[i][M] > target:
                    R -= 1
                elif matrix[i][M] < target:
                    L += 1
                else:
                    return True
        
        return False


