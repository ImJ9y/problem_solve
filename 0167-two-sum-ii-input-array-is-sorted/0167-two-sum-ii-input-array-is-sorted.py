class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers)-1

        while L < R:
            total = numbers[L] + numbers[R]

            if total == target:
                return [L+1,R+1]
            elif total > target:
                R -= 1
            else:
                L += 1
        


                     