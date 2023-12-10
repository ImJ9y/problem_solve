class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]

        return prefix
            