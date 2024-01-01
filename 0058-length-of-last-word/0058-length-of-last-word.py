class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) <= 1:
            return 1
        
        x = s.split(' ')
        wordList = []
        
        for word in x:
            if word != '':
                wordList.append(word)
        
        return len(wordList[len(wordList)-1])