class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_length = max(len(word1), len(word2))
        ans = ""

        for i in range(max_length):
            if len(word1) > i:
                ans += word1[i]
            if len(word2) > i:
                ans += word2[i]
        
        return ans