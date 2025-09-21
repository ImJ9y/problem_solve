class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        len_word = len(words[0])
        len_windowSize = len(words) * len_word

        output = []

        word_freq = {}

        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        
        for i in range(len(s)-len_windowSize+1):
            j = i
            sub_freq = {}
            while j < len_windowSize + i:
                cur_word = s[j:j+len_word]
                if cur_word not in word_freq:
                    break
                
                sub_freq[cur_word] = 1 + sub_freq.get(cur_word, 0)
                if sub_freq[cur_word] > word_freq[cur_word]:
                    break
                
                j += len_word
            
            if j == len_windowSize+i:
                output.append(i)
        
        return output

