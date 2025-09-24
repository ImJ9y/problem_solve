class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        if not s or not words: return []

        word_freq = {}

        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        
        len_word = len(words[0])
        len_window = len_word * len(words)

        output = []


        for i in range(len(s)-len_window+1):
            j = i
            sub_freq = {}

            while j < len_window+i:
                cur_c = s[j:j+len_word]

                if cur_c not in words:
                    break

                sub_freq[cur_c] = 1 + sub_freq.get(cur_c, 0)

                if sub_freq[cur_c] > word_freq[cur_c]:
                    break
                
                j += len_word

            if j == len_window+i:
                output.append(i)
        
        return output