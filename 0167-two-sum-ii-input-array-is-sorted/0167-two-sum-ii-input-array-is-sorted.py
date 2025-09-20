class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers)-1

        while L < R:
            cur = numbers[L] + numbers[R]
            if cur == target:
                return [L+1,R+1]
            elif cur < target:
                L += 1
            else:
                R -= 1