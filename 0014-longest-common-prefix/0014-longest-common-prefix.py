class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for s in strs:
            while s.find(prefix):
                prefix = prefix[:-1]
        
        return prefix