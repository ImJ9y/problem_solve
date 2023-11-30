class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: #if strs is empty - return ""
            return ""
        
        checkWord = strs[0]
        
        for word in strs:
            #if word finds checkWord return 0 if word didn't find the checkWorkd return -1
            while word.find(checkWord) != 0: 
                checkWord = checkWord[:-1]
                if not checkWord: #if we removed all the char return ""
                    return ""
        return checkWord