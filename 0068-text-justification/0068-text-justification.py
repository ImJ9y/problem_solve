class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output = []
        cur_line, cur_length = [], 0

        i = 0

        while i < len(words):
            
            #Line complete
            if cur_length + len(cur_line) + len(words[i]) > maxWidth:       
                extra_space = maxWidth - cur_length
                spaces = extra_space // max(1, len(cur_line)-1)
                remainder = extra_space % max(1, len(cur_line)-1)

                for j in range(max(1, len(cur_line)-1)):
                    cur_line[j] += " " * spaces
                    if remainder != 0:
                        cur_line[j] += " "
                        remainder -= 1
                
                output.append("".join(cur_line))

                #reeset the line and length
                cur_line, cur_length = [], 0


            cur_line.append(words[i])
            cur_length += len(words[i])
            i += 1

        #Handling last line
        last_line = " ".join(cur_line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space

        output.append(last_line)

        return output