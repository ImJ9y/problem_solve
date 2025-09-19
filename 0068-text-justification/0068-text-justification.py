class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        cur_line, cur_len = [], 0
        output = []
        i = 0

        while i < len(words):
            cur_word = words[i]

            #if the line is not completed
            if len(cur_word) + cur_len <= maxWidth:
                cur_len += len(cur_word) + 1 #space
                cur_line.append(cur_word)
                i += 1

            #if the line is compoleted
            else:
                spaces = maxWidth - cur_len + len(cur_line)

                added = 0
                j = 0

                while added < spaces:
                    if j >= len(cur_line)-1:
                        j = 0

                    cur_line[j] += " "
                    j += 1
                    added += 1

                output.append("".join(cur_line))
                cur_line, cur_len = [], 0
        
        last_word = " ".join(cur_line)
        extra_spaces = maxWidth - len(last_word)
        last_word += ' ' * extra_spaces

        output.append(last_word)

        return output 
            

