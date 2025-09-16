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

            if cur_len + len(cur_word) <= maxWidth:
                cur_line.append(cur_word)
                cur_len += len(cur_word) + 1 #adding space
                i += 1
            else:
                #reset our process
                print(cur_line)
                spaces = maxWidth - cur_len + len(cur_line) #total spaces left

                added = 0
                j = 0
                
                while added < spaces: #while we still need to add space
                    if j >= len(cur_line)-1:
                        j = 0
                    
                    cur_line[j] += " "
                    added += 1
                    j += 1
                output.append("".join(cur_line))
                cur_line, cur_len = [], 0
        

        #Handling last line
        last_line = " ".join(cur_line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space

        output.append(last_line)

        return output



