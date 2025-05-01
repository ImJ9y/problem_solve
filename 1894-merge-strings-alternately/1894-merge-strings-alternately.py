class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""

        length = max(len(word1), len(word2))

        for i in range(length):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
    
        return ans