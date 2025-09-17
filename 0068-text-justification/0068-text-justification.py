class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output = []
        cur_line, cur_len = [], 0
        i = 0

        while i < len(words):
            cur_word = words[i]

            #line is not complete
            if cur_len + len(cur_word) <= maxWidth:
                cur_line.append(cur_word)
                cur_len += len(cur_word) + 1 #space
                i += 1
            
            #line is complete
            else:
                spaces = maxWidth - cur_len + len(cur_line)

                j = 0
                added = 0

                while added < spaces:
                    if j >= len(cur_line)-1:
                        j = 0

                    cur_line[j] += ' '
                    added += 1
                    j += 1
                
                output.append("".join(cur_line))
                cur_line, cur_len = [], 0

        last_word = " ".join(cur_line)
        extra_spaces = maxWidth - len(last_word)
        last_word += ' ' * extra_spaces

        output.append(last_word)

        return output


