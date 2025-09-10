class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # array = []

        # while s[-1] == ' ':
        #     s = s[:-1]

        new_s = s.split()

        return " ".join(new_s[::-1])
        